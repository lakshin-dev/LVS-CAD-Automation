from ezdxf.enums import TextEntityAlignment
from constants import *
import math


# ==========================================================
# GLOBAL SCALE
# ==========================================================

def get_global_scale(device_counts):

    maximum = max(device_counts) if device_counts else 0

    if maximum <= DEFAULT_DEVICE_LIMIT:
        return DEFAULT_SCALE

    if maximum <= SHRINK_LIMIT:

        t = (maximum - DEFAULT_DEVICE_LIMIT) / (
            SHRINK_LIMIT - DEFAULT_DEVICE_LIMIT
        )

        return DEFAULT_SCALE - t * (
            DEFAULT_SCALE - MIN_SYMBOL_SCALE
        )

    return MIN_SYMBOL_SCALE


# ==========================================================
# BUILD DETECTOR LIST
# ==========================================================

def build_detector_list(

    smoke,

    heat,

    multi,

    mcp,

    monitor,

    control,

    relay

):

    devices = []

    devices.extend([BLOCK_SMOKE] * smoke)

    devices.extend([BLOCK_HEAT] * heat)

    devices.extend([BLOCK_MULTI] * multi)

    devices.extend([BLOCK_MCP] * mcp)

    devices.extend([BLOCK_MONITOR] * monitor)

    devices.extend([BLOCK_CONTROL] * control)

    devices.extend([BLOCK_RELAY] * relay)

    return devices


# ==========================================================
# BUILD HOOTER LIST
# ==========================================================

def build_hooter_list(

    hooter

):

    return [BLOCK_HOOTER] * hooter


# ==========================================================
# PLACE BLOCK
# ==========================================================

def add_device(

    msp,

    block,

    x,

    y,

    scale

):

    msp.add_blockref(

        block,

        (x, y),

        dxfattribs={

            "xscale": scale,

            "yscale": scale

        }

    )

# ==========================================================
# DRAW BOX
# ==========================================================

def draw_box(

    msp,

    x,

    y,

    width,

    height,

    color

):

    msp.add_lwpolyline(

        [

            (x, y),

            (x + width, y),

            (x + width, y + height),

            (x, y + height)

        ],

        close=True,

        dxfattribs={

            "color": color,

            "lineweight": LW_BORDER

        }

    )


# ==========================================================
# DRAW DEVICE ROW
# ==========================================================

def draw_row(

    msp,

    device_list,

    box_x,

    box_y,

    box_width,

    box_height,

    scale

):

    if not device_list:
        return

    spacing = DEVICE_SPACING * scale

    occupied = SYMBOL_WIDTH * scale

    if len(device_list) > 1:

        occupied += (len(device_list)-1) * spacing

    start_x = box_x + (box_width - occupied) / 2

    center_y = box_y + box_height / 2

    for i, device in enumerate(device_list):

        add_device(

            msp,

            device,

            start_x + i * spacing,

            center_y,

            scale

        )


# ==========================================================
# CALCULATE BOX WIDTH
# ==========================================================

def calculate_box_width(

    count,

    scale

):

    if count == 0:

        return MIN_BOX_WIDTH

    width = SYMBOL_WIDTH * scale

    if count > 1:

        width += (count-1) * DEVICE_SPACING * scale

    width += BOX_PADDING_X * 2

    return max(

        MIN_BOX_WIDTH,

        width

    )


# ==========================================================
# DRAW LABEL
# ==========================================================

def draw_floor_label(

    msp,

    floor_name,

    y

):

    label_x = FLOOR_WIDTH + LABEL_GAP

    msp.add_lwpolyline(

        [

            (label_x, y),

            (label_x + LABEL_BOX_WIDTH, y),

            (label_x + LABEL_BOX_WIDTH, y + FLOOR_HEIGHT),

            (label_x, y + FLOOR_HEIGHT)

        ],

        close=True,

        dxfattribs={

            "color": COLOR_LABEL,

            "lineweight": LW_BORDER

        }

    )

    msp.add_text(

        floor_name,

        height=TEXT_HEIGHT,

        dxfattribs={

            "color": COLOR_LABEL

        }

    ).set_placement(

        (

            label_x + LABEL_BOX_WIDTH/2,

            y + FLOOR_HEIGHT/2

        ),

        align=TextEntityAlignment.MIDDLE_CENTER

    )
# ==========================================================
# DRAW FLOOR
# ==========================================================

def draw_floor(

    msp,

    floor_name,

    y,

    smoke,

    heat,

    multi,

    mcp,

    hooter,

    monitor,

    control,

    relay,

    scale

):

    # ------------------------------------------------------
    # FLOOR BORDER
    # ------------------------------------------------------

    msp.add_lwpolyline(

        [

            (0, y),

            (FLOOR_WIDTH, y),

            (FLOOR_WIDTH, y + FLOOR_HEIGHT),

            (0, y + FLOOR_HEIGHT)

        ],

        close=True,

        dxfattribs={

            "color": COLOR_FLOOR,

            "lineweight": LW_BORDER

        }

    )

    draw_floor_label(

        msp,

        floor_name,

        y

    )

    # ------------------------------------------------------
    # DEVICE LISTS
    # ------------------------------------------------------

    detector_list = build_detector_list(

        smoke,

        heat,

        multi,

        mcp,

        monitor,

        control,

        relay

    )

    hooter_list = build_hooter_list(

        hooter

    )

    # ------------------------------------------------------
    # BOX WIDTHS
    # ------------------------------------------------------

    detector_width = calculate_box_width(

        len(detector_list),

        scale

    )

    hooter_width = calculate_box_width(

        len(hooter_list),

        scale

    )

    # ------------------------------------------------------
    # USE LARGER WIDTH SO BOTH BOXES ALIGN
    # ------------------------------------------------------

    box_width = max(

        detector_width,

        hooter_width

    )

    box_x = (FLOOR_WIDTH - box_width) / 2

    # ------------------------------------------------------
    # VERTICAL LAYOUT
    # ------------------------------------------------------

    total_height = (

        TOP_BOX_HEIGHT +

        BOX_GAP +

        BOTTOM_BOX_HEIGHT

    )

    start_y = y + (

        FLOOR_HEIGHT -

        total_height

    ) / 2

    hooter_y = start_y

    detector_y = (

        hooter_y +

        TOP_BOX_HEIGHT +

        BOX_GAP

    )

    # ------------------------------------------------------
    # DRAW HOOTER BOX
    # ------------------------------------------------------

    draw_box(

        msp,

        box_x,

        hooter_y,

        box_width,

        TOP_BOX_HEIGHT,

        COLOR_HOOTER_BOX

    )

    draw_row(

        msp,

        hooter_list,

        box_x,

        hooter_y,

        box_width,

        TOP_BOX_HEIGHT,

        scale

    )

    # ------------------------------------------------------
    # DRAW DETECTOR BOX
    # ------------------------------------------------------

    draw_box(

        msp,

        box_x,

        detector_y,

        box_width,

        BOTTOM_BOX_HEIGHT,

        COLOR_DEVICE_BOX

    )

    draw_row(

        msp,

        detector_list,

        box_x,

        detector_y,

        box_width,

        BOTTOM_BOX_HEIGHT,

        scale

    )