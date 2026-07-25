"""
Record Label Composer

print_engine.py

Printing engine.
"""

from print_layout import PrintLayout
from PIL import ImageOps
import win32print
import win32ui
from PIL import Image
from PIL import ImageDraw


class PrintEngine:
    """Rendering engine for preview, printing and PDF export."""

    def __init__(self, canvas, artwork_images):
        self.canvas = canvas
        self.artwork_images = artwork_images

    def create_page(self):
        """Create a blank A4 page."""

        page = Image.new(
            "RGB",
            (2480, 3508),
            "white"
        )
        draw = ImageDraw.Draw(page)

        label_positions = PrintLayout.get_label_centres_mm()

        x, y = label_positions[0]

        print(f"x = {x}")
        print(f"y = {y}")

        print(label_positions)
        print()

        print("PrintEngine can see:")

        for i, panel in enumerate(self.artwork_images):
            print(f"Panel {i + 1}:", panel.original_image)

 #        draw.ellipse(
 #           (
 #               50,
 #               50,
 #               1230,
 #               1230
 #           ),
 #           outline="red",
 #           width=6
 #       )

        image = self.artwork_images[0].original_image.copy()

        page.paste(
            image,
            (50, 50)
        )
        draw.ellipse(
            (
                1300,
                100,
                2480,
                1281
            ),
            outline="red",
            width=6
        )

        return page
    
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