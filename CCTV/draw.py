from ezdxf.enums import TextEntityAlignment
from constants import *
import math


# ==========================================================
# CALCULATE GLOBAL SCALE
# ==========================================================

def get_global_scale(floor_camera_counts):
    """
    Calculate a single scale factor that applies to ALL floors.
    Scale is determined by the floor with the MOST cameras.
    """
    max_cameras = max(floor_camera_counts) if floor_camera_counts else 0
    
    if max_cameras <= DEFAULT_CAMERA_LIMIT:
        return 1.0
    
    if max_cameras <= SHRINK_LIMIT:
        t = (max_cameras - DEFAULT_CAMERA_LIMIT) / (
            SHRINK_LIMIT - DEFAULT_CAMERA_LIMIT
        )
        return 1.0 - t * (1.0 - MIN_CAMERA_SCALE)
    
    return MIN_CAMERA_SCALE


# ==========================================================
# CALCULATE ROW LAYOUT
# ==========================================================

def calculate_row_layout(camera_count, scale, camera_box_width):
    """
    Calculate how cameras should be arranged.
    Returns layout info including rows and cameras per row.
    """
    symbol_width = CAMERA_SYMBOL_WIDTH * scale
    spacing = BASE_CAMERA_SPACING * scale
    
    # Check if this needs to be split into 2 boxes
    # Split when camera_count >= SHRINK_LIMIT (24 or more)
    if camera_count >= SHRINK_LIMIT:
        # Split into 2 rows with separate boxes
        row1 = math.ceil(camera_count / 2)
        row2 = camera_count - row1
        
        # Calculate occupied width for each row
        row1_width = symbol_width
        if row1 > 1:
            row1_width += (row1 - 1) * spacing
            
        row2_width = symbol_width
        if row2 > 1:
            row2_width += (row2 - 1) * spacing
        
        return {
            "boxes": 2,
            "row1_count": row1,
            "row2_count": row2,
            "spacing": spacing,
            "symbol_width": symbol_width,
            "row1_width": row1_width,
            "row2_width": row2_width,
            "box_height": CAMERA_BOX_HEIGHT
        }
    
    # Single box layout
    occupied = symbol_width
    if camera_count > 1:
        occupied += (camera_count - 1) * spacing
    
    return {
        "boxes": 1,
        "row1_count": camera_count,
        "row2_count": 0,
        "spacing": spacing,
        "symbol_width": symbol_width,
        "row1_width": occupied,
        "row2_width": 0,
        "box_height": CAMERA_BOX_HEIGHT
    }


# ==========================================================
# DRAW A SINGLE CAMERA BOX WITH CAMERAS
# ==========================================================

def draw_camera_box(msp, x, y, width, height, camera_list, spacing, scale):
    """
    Draw a single camera box with cameras bottom-aligned
    """
    if not camera_list:
        return
    
    # Draw the box
    msp.add_lwpolyline(
        [
            (x, y),
            (x + width, y),
            (x + width, y + height),
            (x, y + height)
        ],
        close=True,
        dxfattribs={"color": COLOR_CAMERA_BOX}
    )
    
    # Calculate camera positions - RIGHT ALIGNED, BOTTOM ALIGNED
    total_width = len(camera_list) * spacing
    if len(camera_list) > 1:
        total_width = (len(camera_list) - 1) * spacing + CAMERA_SYMBOL_WIDTH * scale
    
    start_x = x + width - CAMERA_BOX_PADDING - total_width
    
    # Bottom align cameras
    camera_y = y + height - 50
    
    for i, camera in enumerate(camera_list):
        cam_x = start_x + i * spacing
        add_camera_block(msp, camera, cam_x, camera_y, scale)


# ==========================================================
# DRAW FLOOR
# ==========================================================

def draw_floor(
    msp,
    floor_name,
    y,
    dome_count,
    bullet_count,
    global_scale,
    floor_index=0
):

    total = dome_count + bullet_count
    
    # =====================================================
    # FLOOR
    # =====================================================

    msp.add_lwpolyline(
        [
            (0, y),
            (FLOOR_WIDTH, y),
            (FLOOR_WIDTH, y + FLOOR_HEIGHT),
            (0, y + FLOOR_HEIGHT)
        ],
        close=True,
        dxfattribs={"color": COLOR_FLOOR}
    )

    # =====================================================
    # LABEL
    # =====================================================

    label_x = FLOOR_WIDTH + LABEL_GAP

    msp.add_lwpolyline(
        [
            (label_x, y),
            (label_x + LABEL_BOX_WIDTH, y),
            (label_x + LABEL_BOX_WIDTH, y + FLOOR_HEIGHT),
            (label_x, y + FLOOR_HEIGHT)
        ],
        close=True,
        dxfattribs={"color": COLOR_LABEL}
    )

    msp.add_text(
        floor_name,
        height=TEXT_HEIGHT,
        dxfattribs={"color": COLOR_LABEL}
    ).set_placement(
        (
            label_x + LABEL_BOX_WIDTH / 2,
            y + FLOOR_HEIGHT / 2
        ),
        align=TextEntityAlignment.MIDDLE_CENTER
    )

    if total == 0:
        # Draw electrical box only
        draw_electrical_box(msp, y)
        return

    # =====================================================
    # BUILD CAMERA LIST
    # =====================================================

    camera_list = []
    camera_list.extend(["DOME"] * dome_count)
    camera_list.extend(["BULLET"] * bullet_count)

    # =====================================================
    # CALCULATE LAYOUT
    # =====================================================
    
    # Calculate available width for camera boxes
    # Electrical box is on the RIGHT, so camera boxes are on the LEFT
    # Leave gap between camera area and electrical box
    camera_area_width = FLOOR_WIDTH - 2 * OUTER_MARGIN_X - ELECTRICAL_BOX_WIDTH - CAMERA_TO_ELECTRICAL_GAP - 100
    camera_area_x = OUTER_MARGIN_X
    
    layout = calculate_row_layout(total, global_scale, camera_area_width)
    spacing = layout["spacing"]
    
    if layout["boxes"] == 1:
        # Single box - RIGHT ALIGNED (next to electrical box)
        # Calculate required width based on cameras
        required_width = layout["row1_width"] + 2 * CAMERA_BOX_PADDING
        box_width = max(MIN_CAMERA_BOX_WIDTH, required_width)
        # Don't exceed available width
        if box_width > camera_area_width:
            box_width = camera_area_width
        
        # Right align the box - push it to the right side of the available area
        box_x = camera_area_x + camera_area_width - box_width
        box_y = y + (FLOOR_HEIGHT - layout["box_height"]) / 2
        
        draw_camera_box(
            msp,
            box_x,
            box_y,
            box_width,
            layout["box_height"],
            camera_list,
            spacing,
            global_scale
        )
        
    else:
        # Two separate boxes stacked vertically - RIGHT ALIGNED
        # Calculate required width based on the wider row
        max_row_width = max(layout["row1_width"], layout["row2_width"])
        required_width = max_row_width + 2 * CAMERA_BOX_PADDING
        box_width = max(MIN_CAMERA_BOX_WIDTH, required_width)
        # Don't exceed available width
        if box_width > camera_area_width:
            box_width = camera_area_width
        
        row1_list = camera_list[:layout["row1_count"]]
        row2_list = camera_list[layout["row1_count"]:]
        
        # Right align the boxes
        box_x = camera_area_x + camera_area_width - box_width
        
        # Calculate total height needed for 2 boxes with gap
        total_box_height = 2 * layout["box_height"] + CAMERA_BOX_GAP
        
        # Center the two boxes vertically in the floor
        start_y = y + (FLOOR_HEIGHT - total_box_height) / 2
        
        # Box 1 (Top) - NO LABEL
        box1_y = start_y
        draw_camera_box(
            msp,
            box_x,
            box1_y,
            box_width,
            layout["box_height"],
            row1_list,
            spacing,
            global_scale
        )
        
        # Box 2 (Bottom) - NO LABEL
        box2_y = start_y + layout["box_height"] + CAMERA_BOX_GAP
        draw_camera_box(
            msp,
            box_x,
            box2_y,
            box_width,
            layout["box_height"],
            row2_list,
            spacing,
            global_scale
        )

    # =====================================================
    # ELECTRICAL BOX (Right side with gap)
    # =====================================================
    
    draw_electrical_box(msp, y)


def draw_electrical_box(msp, y):
    """Draw the electrical box on the right side with gap from camera box"""
    
    # Leave gap between camera area and electrical box
    camera_area_width = FLOOR_WIDTH - 2 * OUTER_MARGIN_X - ELECTRICAL_BOX_WIDTH - CAMERA_TO_ELECTRICAL_GAP - 100
    camera_area_x = OUTER_MARGIN_X
    
    # Position electrical box to the right of the camera area with CLEAR gap
    elec_box_x = camera_area_x + camera_area_width + CAMERA_TO_ELECTRICAL_GAP + 50
    elec_box_y = y + (FLOOR_HEIGHT - ELECTRICAL_BOX_HEIGHT) / 2
    
    msp.add_blockref(
        "ELECTRICAL_BOX",
        (elec_box_x + ELECTRICAL_BOX_WIDTH/2, elec_box_y + ELECTRICAL_BOX_HEIGHT/2),
        dxfattribs={
            "color": COLOR_ELECTRICAL_BOX,
            "xscale": 1.0,
            "yscale": 1.0
        }
    )


def add_camera_block(msp, camera_type, x, y, scale):
    """Helper function to add camera blocks with consistent color and scale"""
    
    if camera_type == "DOME":
        msp.add_blockref(
            "DOME",
            (x, y),
            dxfattribs={
                "color": COLOR_DOME,
                "xscale": scale,
                "yscale": scale
            }
        )
    else:  # BULLET
        msp.add_blockref(
            "BULLET",
            (x, y),
            dxfattribs={
                "color": COLOR_BULLET,
                "xscale": scale,
                "yscale": scale
            }
        )