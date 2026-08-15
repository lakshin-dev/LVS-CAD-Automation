# ======================================================
# CCTV GENERATOR v1.0
# Constants
# ======================================================

# ======================================================
# CAMERA LIMITS
# ======================================================

# Cameras displayed at full size
DEFAULT_CAMERA_LIMIT = 16

# Begin shrinking after 16
SHRINK_LIMIT = 24

# Two-row layout begins after this
DOUBLE_ROW_LIMIT = 24

# Absolute limit (for now)
MAX_CAMERAS = 48


# ======================================================
# BASE CAMERA GEOMETRY
# ======================================================

BASE_CAMERA_SIZE = 0.70

BASE_CAMERA_SPACING = 300

CAMERA_SYMBOL_WIDTH = 75


# ======================================================
# FLOOR
# ======================================================

FLOOR_WIDTH = 5500

FLOOR_HEIGHT = 1200

OUTER_MARGIN_X = 250
OUTER_MARGIN_Y = 180


# ======================================================
# FLOOR LABEL
# ======================================================

LABEL_BOX_WIDTH = 800
LABEL_GAP = 150

TEXT_HEIGHT = 50


# ======================================================
# CAMERA BOX
# ======================================================

CAMERA_BOX_PADDING = 180

CAMERA_BOX_HEIGHT = 200  # Reduced height for single row

MIN_CAMERA_BOX_WIDTH = 700


# ======================================================
# TWO ROW LAYOUT
# ======================================================

# Gap between two camera boxes when stacked (for wire routing)
CAMERA_BOX_GAP = 100  # Increased for wire routing space


# ======================================================
# SCALING
# ======================================================

# Never shrink below this
MIN_CAMERA_SCALE = 0.65


# ======================================================
# ELECTRICAL BOX
# ======================================================

ELECTRICAL_BOX_WIDTH = 200
ELECTRICAL_BOX_HEIGHT = 300

# Gap between camera box and electrical box
CAMERA_TO_ELECTRICAL_GAP = 100


# ======================================================
# COLORS
# ======================================================

COLOR_FLOOR = 7

COLOR_LABEL = 4

COLOR_CAMERA_BOX = 8

COLOR_DOME = 2

COLOR_BULLET = 1

COLOR_WIRE = 5

COLOR_RISER = 6

COLOR_EQUIPMENT = 3

COLOR_ELECTRICAL_BOX = 3