"""
Record Label Composer
Version 0.3.0b
Build 003

guides.py

Functions for drawing record label guides.
"""

class LabelGuides:
    """Draws the record label guides."""

    @staticmethod
    def draw_guides(canvas):

        width = canvas.winfo_width()
        height = canvas.winfo_height()

        centre_x = width / 2
        centre_y = height / 2

        radius = min(width, height) * 0.38

        # Bleed guide
        canvas.create_oval(
            centre_x - radius,
            centre_y - radius,
            centre_x + radius,
            centre_y + radius,
            outline="red",
            dash=(6, 4),
        )

        # Cut guide
        cut = radius * 0.96

        canvas.create_oval(
            centre_x - cut,
            centre_y - cut,
            centre_x + cut,
            centre_y + cut,
            outline="white",
        )

        # Safe area
        safe = radius * 0.82

        canvas.create_oval(
            centre_x - safe,
            centre_y - safe,
            centre_x + safe,
            centre_y + safe,
            outline="lime",
            dash=(3, 3),
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
        )