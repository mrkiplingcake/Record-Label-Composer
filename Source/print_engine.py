"""
Record Label Composer

print_engine.py

Printing engine.
"""

from print_layout import PrintLayout
import win32print
import win32ui
from PIL import ImageGrab


class PrintEngine:
    """Rendering engine for preview, printing and PDF export."""

    def __init__(self, canvas):
        self.canvas = canvas

    def get_canvas_image(self):
        """Capture the canvas as a PIL image."""

        self.canvas.update()

        x = self.canvas.winfo_rootx()
        y = self.canvas.winfo_rooty()

        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        return ImageGrab.grab(
            bbox=(
                x,
                y,
                x + width,
                y + height
            )
        )   

    def draw_page(self):
        """Draw the paper."""

        self.canvas.create_rectangle(
            0,
            0,
            self.canvas.paper_width_pixels,
            self.canvas.paper_height_pixels,
            fill="white",
            outline="light grey"
        )