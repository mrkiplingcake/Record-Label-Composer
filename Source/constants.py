"""
Record Label Composer
Build 002 - Workbench

constants.py
Application-wide constants used throughout the program.
"""

APP_NAME = "Record Label Composer"
APP_TAGLINE = "Designed for precision 100 mm vinyl centre labels"

VERSION = "0.2.0"
BUILD = "002"
BUILD_NAME = "Workbench"

WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 750
MIN_WINDOW_WIDTH = 900
MIN_WINDOW_HEIGHT = 600

BACKGROUND_COLOUR = "#ECE8DD"
PANEL_BACKGROUND = "#F8F8F8"
PANEL_BORDER = "#B0B0B0"

LABEL_DIAMETER_MM = 100.0
CENTRE_HOLE_MM = 7.26

STATUS_READY = "Ready"

ABOUT_TEXT = (
    f"{APP_NAME}\n"
    f"Build {BUILD} – {BUILD_NAME}\n\n"
    f"{APP_TAGLINE}"
)
