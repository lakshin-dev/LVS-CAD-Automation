import math
from constants import *
from ezdxf.enums import TextEntityAlignment

# =====================================================
# DOME CAMERA BLOCK
# =====================================================

def create_dome_block(doc):

    if "DOME" in doc.blocks:
        return

    block = doc.blocks.new("DOME")

    r = 90 * BASE_CAMERA_SIZE

    # ---------------------------------
    # Outer Arc
    # ---------------------------------

    points = []

    for angle in range(180, 361, 5):

        rad = math.radians(angle)

        x = r * math.cos(rad)
        y = r * math.sin(rad)

        points.append((x, y))

    block.add_lwpolyline(
        points,
        dxfattribs={"color": 0}
    )

    # ---------------------------------
    # Top Rectangle
    # ---------------------------------

    h = 45 * BASE_CAMERA_SIZE

    block.add_lwpolyline(

        [

            (-r, 0),

            ( r, 0),

            ( r, h),

            (-r, h)

        ],

        close=True,

        dxfattribs={"color":0}

    )

    # ---------------------------------
    # Lens
    # ---------------------------------

    block.add_circle(

        (0, -35 * BASE_CAMERA_SIZE),

        22 * BASE_CAMERA_SIZE,

        dxfattribs={"color":0}

    )


# =====================================================
# BULLET CAMERA BLOCK
# =====================================================

def create_bullet_block(doc):

    if "BULLET" in doc.blocks:
        return

    block = doc.blocks.new("BULLET")

    body_w = 70 * BASE_CAMERA_SIZE
    body_h = 140 * BASE_CAMERA_SIZE

    # ---------------------------------
    # Camera Body
    # ---------------------------------

    block.add_lwpolyline(

        [

            (-body_w/2, body_h/2),

            ( body_w/2, body_h/2),

            ( body_w/2,-body_h/2),

            (-body_w/2,-body_h/2)

        ],

        close=True,

        dxfattribs={"color":0}

    )

    # ---------------------------------
    # Hatch Lines
    # ---------------------------------

    step = 18 * BASE_CAMERA_SIZE

    y = body_h/2 - step

    while y > -body_h/2:

        block.add_line(

            (-body_w/2, y),

            ( body_w/2, y-step),

            dxfattribs={"color":0}

        )

        y -= step

    # ---------------------------------
    # Field Of View
    # ---------------------------------

    origin = (0, -body_h/2)

    for radius in [35, 55, 75]:

        block.add_arc(

            center=origin,

            radius=radius * BASE_CAMERA_SIZE,

            start_angle=240,

            end_angle=300,

            dxfattribs={"color":0}

        )


# =====================================================
# ELECTRICAL BOX BLOCK (Simplified with label outside)
# =====================================================

def create_electrical_box_block(doc):

    if "ELECTRICAL_BOX" in doc.blocks:
        return

    block = doc.blocks.new("ELECTRICAL_BOX")

    w = ELECTRICAL_BOX_WIDTH
    h = ELECTRICAL_BOX_HEIGHT

    # ---------------------------------
    # Electrical Box Body - Simple Rectangle
    # ---------------------------------

    block.add_lwpolyline(

        [

            (-w/2, -h/2),
            (w/2, -h/2),
            (w/2, h/2),
            (-w/2, h/2)

        ],

        close=True,

        dxfattribs={
            "color": COLOR_ELECTRICAL_BOX,
            "lineweight": 60
        }

    )

    # ---------------------------------
    # "ELECTRICAL BOX" Label ABOVE the box
    # ---------------------------------

    text = block.add_text(
        "ELECTRICAL",
        height=30,
        dxfattribs={"color": COLOR_ELECTRICAL_BOX}
    )
    text.set_placement(
        (0, h/2 + 40),
        align=TextEntityAlignment.MIDDLE_CENTER
    )

    text2 = block.add_text(
        "BOX",
        height=30,
        dxfattribs={"color": COLOR_ELECTRICAL_BOX}
    )
    text2.set_placement(
        (0, h/2 + 10),
        align=TextEntityAlignment.MIDDLE_CENTER
    )

    # ---------------------------------
    # Simple internal line (just for visual)
    # ---------------------------------

    block.add_line(
        (-w/2 + 20, 0),
        (w/2 - 20, 0),
        dxfattribs={"color": COLOR_ELECTRICAL_BOX}
    )


# =====================================================
# CREATE ALL BLOCKS
# =====================================================

def create_all_blocks(doc):
    create_dome_block(doc)
    create_bullet_block(doc)
    create_electrical_box_block(doc)