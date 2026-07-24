"""
Record Label Composer

artwork_panel.py
Artwork panel widget.
"""

from pathlib import Path
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog

from constants import PANEL_BACKGROUND, PANEL_BORDER
from guides import LabelGuides


class ArtworkPanel(tk.Frame):
    """Artwork panel."""

    def __init__(self, master, panel_number: int):
        super().__init__(
            master,
            bg=PANEL_BACKGROUND,
            highlightbackground=PANEL_BORDER,
            highlightthickness=1,
            bd=0,
        )

        self.panel_number = panel_number
        self.image_path = None
        self.photo = None

        self.image_x = 0
        self.image_y = 0

        self.drag_start_x = 0
        self.drag_start_y = 0

        title = tk.Label(
            self,
            text=f"Artwork Panel {panel_number}",
            font=("Segoe UI", 11, "bold"),
            bg=PANEL_BACKGROUND,
        )
        title.pack(pady=(20, 10))

        self.canvas = tk.Canvas(
    self,
    bg=PANEL_BACKGROUND,
    highlightthickness=0
)

        self.canvas.pack(
    expand=True,
    fill="both",
    padx=20,
    pady=20
)

        self.canvas.create_text(
    200,
    130,
    text="Double-click here\nto load artwork",
    justify="center",
    fill="white",
    font=("Segoe UI", 10),
)

        self.bind("<Double-Button-1>", self.load_artwork)
        self.canvas.bind("<Double-Button-1>", self.load_artwork)
        self.canvas.bind("<Button-1>", self.start_drag)
        self.canvas.bind("<B1-Motion>", self.drag_image)

    def load_artwork(self, event=None):

        filename = filedialog.askopenfilename(
            title="Select Artwork",
            filetypes=[
                ("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif *.tif *.tiff"),
                ("All Files", "*.*"),
            ],
        )

        if not filename:
            return

        self.image_path = filename

        image = Image.open(filename)

        image.thumbnail((420, 260))

        self.photo = ImageTk.PhotoImage(image)

        self.canvas.delete("all")

        self.canvas.update_idletasks()

        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        centre_x = canvas_width // 2
        centre_y = canvas_height // 2

        self.canvas.create_image(
            centre_x,
            centre_y,
            image=self.photo
    )

        self.canvas.image = self.photo

        LabelGuides.draw_guides(self.canvas)
    def start_drag(self, event):
        """Remember where the mouse started."""

        self.drag_start_x = event.x
        self.drag_start_y = event.y


    def drag_image(self, event):
        """Drag the artwork."""

        print("Dragging...")