"""
Record Label Composer

print_preview.py

Print preview window.
"""
import win32print
import win32ui
import tkinter as tk
from print_layout import PrintLayout

from print_engine import PrintEngine


class PrintPreview(tk.Toplevel):
    """Print preview window."""

    def __init__(self, parent):
        super().__init__(parent)

        self.title("Print Preview")

        self.print_button = tk.Button(
        self,
        text="Print",
        width=12,
        command=self.print_preview,
    )

        self.print_button.pack(pady=5)

        self.geometry("900x700")

        self.configure(bg="#606060")

        self.canvas = tk.Canvas(
        self,
        bg="#606060",
        highlightthickness=0,
    )
        self.engine = PrintEngine(self.canvas)

        self.canvas.pack(fill="both", expand=True)

        available_width = 900 - 40
        available_height = 700 - 40

        pixels_per_mm = min(
            available_width / PrintLayout.PAGE_WIDTH_MM,
            available_height / PrintLayout.PAGE_HEIGHT_MM,
        )

        page_width = 210 * pixels_per_mm
        page_height = 297 * pixels_per_mm

        label_diameter = PrintLayout.LABEL_DIAMETER_MM * pixels_per_mm
        label_radius = label_diameter / 2

        left = (900 - page_width) / 2
        top = (700 - page_height) / 2

        """template_left = left + (PrintLayout.TEMPLATE_LEFT_MM * pixels_per_mm)
        template_top = top + (PrintLayout.TEMPLATE_TOP_MM * pixels_per_mm)
        """
        template_left = left
        template_top = top


        self.canvas.create_rectangle(
            left,
            top,
            left + page_width,
            top + page_height,
            fill="white",
            outline="#c0c0c0",
            width=2,
        )

        # Draw the four label positions
        for x, y in PrintLayout.get_label_centres_mm():


            self.canvas.create_oval(
                template_left + (x * pixels_per_mm) - label_radius,
                template_top + (y * pixels_per_mm) - label_radius,

                template_left + (x * pixels_per_mm) + label_radius,
                template_top + (y * pixels_per_mm) + label_radius,
                outline="blue",
                width=2,
            )

    def print_preview(self):
        image = self.engine.get_canvas_image()

        image.save("preview.png")

        print("Saved preview.png")