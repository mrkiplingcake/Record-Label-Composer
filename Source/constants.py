"""
Record Label Composer
Build 002 - Workbench

constants.py
Application-wide constants used throughout the program.
"""

APP_NAME = "Record Label Composer"
APP_TAGLINE = "Designed for precision 100 mm vinyl centre labels"

VERSION = "0.4.0"
BUILD = "004"
BUILD_NAME = "Artwork Workspace"

WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 750
MIN_WINDOW_WIDTH = 900
MIN_WINDOW_HEIGHT = 600

BACKGROUND_COLOUR = "#ECE8DD"
PANEL_BACKGROUND = "#F8F8F8"
PANEL_BORDER = "#B0B0B0"

STATUS_READY = "Ready"

ABOUT_TEXT = (
    f"{APP_NAME}\n"
    f"Build {BUILD} – {BUILD_NAME}\n\n"
    f"{APP_TAGLINE}"
)
# Record label guide colours

BLEED_COLOUR = "#ff4040"
CUT_COLOUR = "#1e05fc"
SAFE_COLOUR = "#00ff80"
CENTRE_HOLE_COLOUR = "#ffffff"

# Record label geometry

LABEL_DIAMETER_MM = 100.0
BLEED_MM = 2.0
WORKING_DIAMETER_MM = LABEL_DIAMETER_MM + (BLEED_MM * 2)

SAFE_MARGIN_MM = 5.0
SPINDLE_HOLE_MM = 7.26

WORKING_DIAMETER_MM = 104.0
WORKSPACE_DIAMETER_MM = 110