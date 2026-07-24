"""
Record Label Composer
Version 0.3.0b
Build 003

guides.py

Functions for drawing record label guides.
"""
from geometry import LabelGeometry
from constants import BLEED_COLOUR, CUT_COLOUR, SAFE_COLOUR

class LabelGuides:
    """Draws the record label guides."""

    
    @staticmethod
    def draw_guides(canvas):

        width = canvas.winfo_width()
        height = canvas.winfo_height()

        centre_x = width / 2
        centre_y = height / 2

        radius = LabelGeometry.get_working_radius_pixels(canvas)
        # Bleed guide
        canvas.create_oval(
            centre_x - radius,
            centre_y - radius,
            centre_x + radius,
            centre_y + radius,
            outline=BLEED_COLOUR,
            dash=(6, 4),
            tags=("label",)
        )

        # Cut guide (100 mm)
        cut = radius * (100 / 104)

        canvas.create_oval(
            centre_x - cut,
            centre_y - cut,
            centre_x + cut,
            centre_y + cut,
            outline=CUT_COLOUR,
            tags=("label",)
        )

        # Safe area (95 mm)
        safe = radius * (95 / 104)

        canvas.create_oval(
            centre_x - safe,
            centre_y - safe,
            centre_x + safe,
            centre_y + safe,
            outline=SAFE_COLOUR,
            dash=(3, 3),
            tags=("label",)
        )

        # Centre hole
        hole = 4

        canvas.create_oval(
            centre_x - hole,
            centre_y - hole,
            centre_x + hole,
            centre_y + hole,
            fill="white",
            outline="black",
            tags=("label",)
        )