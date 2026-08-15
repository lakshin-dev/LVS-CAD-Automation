# ==========================================================
# FIRE ALARM SLD GENERATOR
# constants.py
# ==========================================================

# ==========================================================
# DRAWING
# ==========================================================

DRAWING_NAME = "Fire Alarm SLD"
DXF_VERSION = "R2018"

# ==========================================================
# FLOOR
# ==========================================================

FLOOR_WIDTH = 7200
FLOOR_HEIGHT = 1900

OUTER_MARGIN_X = 250
OUTER_MARGIN_Y = 180

# ==========================================================
# LABEL
# ==========================================================

LABEL_BOX_WIDTH = 900
LABEL_GAP = 180

TEXT_HEIGHT = 55
SMALL_TEXT_HEIGHT = 35
TITLE_TEXT_HEIGHT = 90

# ==========================================================
# DEVICE BOXES
# ==========================================================

MIN_BOX_WIDTH = 1000

BOX_PADDING_X = 180
BOX_PADDING_Y = 80

DEVICE_SPACING = 260

SYMBOL_WIDTH = 120

TOP_BOX_HEIGHT = 260        # Hooters
BOTTOM_BOX_HEIGHT = 340     # Detectors

BOX_GAP = 180               # Wire routing space

DOUBLE_ROW_LIMIT = 28

MIN_SYMBOL_SCALE = 0.65

# ==========================================================
# SYMBOL SIZE
# ==========================================================

SMOKE_RADIUS = 60
HEAT_RADIUS = 60
MULTI_RADIUS = 60

MCP_SIZE = 110

HOOTER_RADIUS = 60

MODULE_WIDTH = 140
MODULE_HEIGHT = 90

# ==========================================================
# BLOCK NAMES
# ==========================================================

BLOCK_SMOKE = "SMOKE"

BLOCK_HEAT = "HEAT"

BLOCK_MULTI = "MULTI"

BLOCK_MCP = "MCP"

BLOCK_HOOTER = "HOOTER"

BLOCK_MONITOR = "MONITOR"

BLOCK_CONTROL = "CONTROL"

BLOCK_RELAY = "RELAY"

# ==========================================================
# LAYERS
# ==========================================================

LAYER_BORDER = "BORDER"

LAYER_DEVICE = "DEVICE"

LAYER_TEXT = "TEXT"

LAYER_WIRE = "WIRE"

# ==========================================================
# BORDER COLORS
# ==========================================================

COLOR_FLOOR = 7

COLOR_LABEL = 7

COLOR_HOOTER_BOX = 1

COLOR_DEVICE_BOX = 3

COLOR_WIRE = 8

# ==========================================================
# BLOCK COLORS
# ==========================================================

# Smoke
COLOR_SMOKE_OUTER = 7
COLOR_SMOKE_INNER = 4
COLOR_SMOKE_CENTER = 1

# Heat
COLOR_HEAT_OUTER = 30
COLOR_HEAT_INNER = 2

# Multi Sensor
COLOR_MULTI_OUTER = 4
COLOR_MULTI_INNER = 7
COLOR_MULTI_CENTER = 6

# MCP
COLOR_MCP_OUTER = 2
COLOR_MCP_INNER = 1
COLOR_MCP_TEXT = 7

# Hooter
COLOR_HOOTER_OUTER = 1
COLOR_HOOTER_INNER = 7

# Monitor Module
COLOR_MONITOR_OUTER = 6
COLOR_MONITOR_TEXT = 7

# Control Module
COLOR_CONTROL_OUTER = 5
COLOR_CONTROL_TEXT = 7

# Relay Module
COLOR_RELAY_OUTER = 32
COLOR_RELAY_TEXT = 7

# ==========================================================
# LINEWEIGHTS
# ==========================================================

LW_BORDER = 50

LW_SYMBOL = 30

LW_WIRE = 20

# ==========================================================
# SCALE
# ==========================================================

DEFAULT_SCALE = 1.0

DEFAULT_DEVICE_LIMIT = 20

SHRINK_LIMIT = 40

# ==========================================================
# FILE
# ==========================================================

OUTPUT_FILE = "FIRE_ALARM_LAYOUT.dxf"