import math
from constants import *
from ezdxf.enums import TextEntityAlignment


# =====================================================
# SMOKE DETECTOR
# =====================================================

def create_smoke_block(doc):

    if BLOCK_SMOKE in doc.blocks:
        return

    block = doc.blocks.new(BLOCK_SMOKE)

    r = SMOKE_RADIUS

    # Outer Circle
    block.add_circle(
        (0, 0),
        r,
        dxfattribs={"color": COLOR_SMOKE_OUTER}
    )

    # Cross
    block.add_line(
        (-r*0.70, -r*0.70),
        ( r*0.70,  r*0.70),
        dxfattribs={"color": COLOR_SMOKE_INNER}
    )

    block.add_line(
        (-r*0.70,  r*0.70),
        ( r*0.70, -r*0.70),
        dxfattribs={"color": COLOR_SMOKE_INNER}
    )

    # Centre Dot
    block.add_circle(
        (0,0),
        5,
        dxfattribs={"color": COLOR_SMOKE_CENTER}
    )


# =====================================================
# HEAT DETECTOR
# =====================================================

def create_heat_block(doc):

    if BLOCK_HEAT in doc.blocks:
        return

    block = doc.blocks.new(BLOCK_HEAT)

    r = HEAT_RADIUS

    block.add_circle(
        (0,0),
        r,
        dxfattribs={"color": COLOR_HEAT_OUTER}
    )

    for angle in [0,45,90,135]:

        rad = math.radians(angle)

        x = r * 0.80 * math.cos(rad)
        y = r * 0.80 * math.sin(rad)

        block.add_line(
            (-x,-y),
            ( x, y),
            dxfattribs={"color": COLOR_HEAT_INNER}
        )


# =====================================================
# MULTI SENSOR DETECTOR
# =====================================================

def create_multi_block(doc):

    if BLOCK_MULTI in doc.blocks:
        return

    block = doc.blocks.new(BLOCK_MULTI)

    r = MULTI_RADIUS

    # Outer Circle
    block.add_circle(
        (0,0),
        r,
        dxfattribs={"color": COLOR_MULTI_OUTER}
    )

    # Inner Circle
    block.add_circle(
        (0,0),
        r*0.45,
        dxfattribs={"color": COLOR_MULTI_INNER}
    )

    # Cross
    block.add_line(
        (-r*0.75,0),
        ( r*0.75,0),
        dxfattribs={"color": COLOR_MULTI_INNER}
    )

    block.add_line(
        (0,-r*0.75),
        (0, r*0.75),
        dxfattribs={"color": COLOR_MULTI_INNER}
    )

    # Centre Dot
    block.add_circle(
        (0,0),
        4,
        dxfattribs={"color": COLOR_MULTI_CENTER}
    )

# =====================================================
# MANUAL CALL POINT (MCP)
# =====================================================

def create_mcp_block(doc):

    if BLOCK_MCP in doc.blocks:
        return

    block = doc.blocks.new(BLOCK_MCP)

    s = MCP_SIZE

    # Outer Box
    block.add_lwpolyline(
        [
            (-s/2, -s/2),
            ( s/2, -s/2),
            ( s/2,  s/2),
            (-s/2,  s/2)
        ],
        close=True,
        dxfattribs={"color": COLOR_MCP_OUTER}
    )

    # Inner Circle
    block.add_circle(
        (0, 0),
        s * 0.22,
        dxfattribs={"color": COLOR_MCP_INNER}
    )

    # Cross
    block.add_line(
        (-s*0.18, 0),
        ( s*0.18, 0),
        dxfattribs={"color": COLOR_MCP_INNER}
    )

    block.add_line(
        (0, -s*0.18),
        (0,  s*0.18),
        dxfattribs={"color": COLOR_MCP_INNER}
    )

    # MCP Label
    txt = block.add_text(
        "MCP",
        height=18,
        dxfattribs={"color": COLOR_MCP_TEXT}
    )

    txt.set_placement(
        (0, -s/2 - 22),
        align=TextEntityAlignment.MIDDLE_CENTER
    )


# =====================================================
# HOOTER
# =====================================================

def create_hooter_block(doc):

    if BLOCK_HOOTER in doc.blocks:
        return

    block = doc.blocks.new(BLOCK_HOOTER)

    r = HOOTER_RADIUS

    # Main Circle
    block.add_circle(
        (0,0),
        r,
        dxfattribs={"color": COLOR_HOOTER_OUTER}
    )

    # Speaker Cone
    block.add_circle(
        (0,0),
        r*0.30,
        dxfattribs={"color": COLOR_HOOTER_INNER}
    )

    # Sound Waves
    for radius in [r+12, r+24]:

        block.add_arc(
            center=(0,0),
            radius=radius,
            start_angle=-45,
            end_angle=45,
            dxfattribs={"color": COLOR_HOOTER_OUTER}
        )

    # Centre Dot
    block.add_circle(
        (0,0),
        3,
        dxfattribs={"color": COLOR_HOOTER_INNER}
    )


# =====================================================
# MONITOR MODULE
# =====================================================

def create_monitor_block(doc):

    if BLOCK_MONITOR in doc.blocks:
        return

    block = doc.blocks.new(BLOCK_MONITOR)

    w = MODULE_WIDTH
    h = MODULE_HEIGHT

    # Module Body
    block.add_lwpolyline(
        [
            (-w/2,-h/2),
            ( w/2,-h/2),
            ( w/2, h/2),
            (-w/2, h/2)
        ],
        close=True,
        dxfattribs={"color": COLOR_MONITOR_OUTER}
    )

    # Terminal Pads
    block.add_circle(
        (-w*0.35,0),
        4,
        dxfattribs={"color": COLOR_MONITOR_OUTER}
    )

    block.add_circle(
        ( w*0.35,0),
        4,
        dxfattribs={"color": COLOR_MONITOR_OUTER}
    )

    # Label
    txt = block.add_text(
        "MM",
        height=24,
        dxfattribs={"color": COLOR_MONITOR_TEXT}
    )

    txt.set_placement(
        (0,0),
        align=TextEntityAlignment.MIDDLE_CENTER
    )

# =====================================================
# CONTROL MODULE
# =====================================================

def create_control_block(doc):

    if BLOCK_CONTROL in doc.blocks:
        return

    block = doc.blocks.new(BLOCK_CONTROL)

    w = MODULE_WIDTH
    h = MODULE_HEIGHT

    # Body
    block.add_lwpolyline(
        [
            (-w/2,-h/2),
            ( w/2,-h/2),
            ( w/2, h/2),
            (-w/2, h/2)
        ],
        close=True,
        dxfattribs={"color": COLOR_CONTROL_OUTER}
    )

    # Terminal Pads
    block.add_circle(
        (-w*0.35,0),
        4,
        dxfattribs={"color": COLOR_CONTROL_OUTER}
    )

    block.add_circle(
        (w*0.35,0),
        4,
        dxfattribs={"color": COLOR_CONTROL_OUTER}
    )

    # Control Symbol (Output Arrow)
    block.add_line(
        (-18,0),
        (12,0),
        dxfattribs={"color": COLOR_CONTROL_OUTER}
    )

    block.add_line(
        (12,0),
        (2,8),
        dxfattribs={"color": COLOR_CONTROL_OUTER}
    )

    block.add_line(
        (12,0),
        (2,-8),
        dxfattribs={"color": COLOR_CONTROL_OUTER}
    )

    # Label
    txt = block.add_text(
        "CM",
        height=22,
        dxfattribs={"color": COLOR_CONTROL_TEXT}
    )

    txt.set_placement(
        (0,-28),
        align=TextEntityAlignment.MIDDLE_CENTER
    )


# =====================================================
# RELAY MODULE
# =====================================================

def create_relay_block(doc):

    if BLOCK_RELAY in doc.blocks:
        return

    block = doc.blocks.new(BLOCK_RELAY)

    w = MODULE_WIDTH
    h = MODULE_HEIGHT

    # Body
    block.add_lwpolyline(
        [
            (-w/2,-h/2),
            ( w/2,-h/2),
            ( w/2, h/2),
            (-w/2, h/2)
        ],
        close=True,
        dxfattribs={"color": COLOR_RELAY_OUTER}
    )

    # Relay Contact
    block.add_line(
        (-22,10),
        (-5,-10),
        dxfattribs={"color": COLOR_RELAY_OUTER}
    )

    block.add_line(
        (5,10),
        (22,10),
        dxfattribs={"color": COLOR_RELAY_OUTER}
    )

    block.add_line(
        (5,-10),
        (22,-10),
        dxfattribs={"color": COLOR_RELAY_OUTER}
    )

    # Terminal Pads
    block.add_circle(
        (-w*0.35,0),
        4,
        dxfattribs={"color": COLOR_RELAY_OUTER}
    )

    block.add_circle(
        (w*0.35,0),
        4,
        dxfattribs={"color": COLOR_RELAY_OUTER}
    )

    # Label
    txt = block.add_text(
        "RM",
        height=22,
        dxfattribs={"color": COLOR_RELAY_TEXT}
    )

    txt.set_placement(
        (0,-28),
        align=TextEntityAlignment.MIDDLE_CENTER
    )


# =====================================================
# CREATE ALL BLOCKS
# =====================================================

def create_all_blocks(doc):

    create_smoke_block(doc)

    create_heat_block(doc)

    create_multi_block(doc)

    create_mcp_block(doc)

    create_hooter_block(doc)

    create_monitor_block(doc)

    create_control_block(doc)

    create_relay_block(doc)