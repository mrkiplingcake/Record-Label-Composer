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

        title = tk.Label(
            self,
            text=f"Artwork Panel {panel_number}",
            font=("Segoe UI", 11, "bold"),
            bg=PANEL_BACKGROUND,
        )
        title.pack(pady=(20, 10))

        self.preview = tk.Label(
            self,
            text="Double-click here\nto load artwork",
            justify="center",
            font=("Segoe UI", 10),
            bg=PANEL_BACKGROUND,
        )
        self.preview.pack(expand=True, fill="both", padx=20, pady=20)

        self.bind("<Double-Button-1>", self.load_artwork)
        self.preview.bind("<Double-Button-1>", self.load_artwork)

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

        self.preview.config(
            image=self.photo,
            text=""
        )

        self.preview.image = self.photo