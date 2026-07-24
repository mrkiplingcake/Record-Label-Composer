"""
Record Label Composer

artwork_panel.py
Artwork panel widget.
"""

from pathlib import Path
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog

from constants import PANEL_BACKGROUND, PANEL_BORDER, WORKING_DIAMETER_MM
from guides import LabelGuides
from geometry import LabelGeometry


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
        self.original_image = None
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

        self.original_image = Image.open(filename)

        self.display_image()

    def display_image(self):

        self.canvas.delete("all")

        self.canvas.update_idletasks()

        if self.original_image is None:
            return

        image = self.original_image.copy()

        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        guide_radius = LabelGeometry.get_working_radius_pixels(self.canvas)

        image.thumbnail(
            (int(guide_radius * 2), int(guide_radius * 2)),
            Image.Resampling.LANCZOS
        )

        self.photo = ImageTk.PhotoImage(image)

        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        centre_x = canvas_width // 2
        centre_y = canvas_height // 2
        self.image_x = centre_x
        self.image_y = centre_y

        self.image_id = self.canvas.create_image(
        centre_x,
        centre_y,
        image=self.photo,
        tags=("label", "artwork")
    )
        self.canvas.tag_bind("artwork", "<Button-1>", self.start_drag)
        self.canvas.tag_bind("artwork", "<B1-Motion>", self.drag_image)
        self.canvas.tag_bind("artwork", "<Enter>", lambda e: self.canvas.config(cursor="fleur"))
        self.canvas.tag_bind("artwork", "<Leave>", lambda e: self.canvas.config(cursor=""))

        self.canvas.image = self.photo

        LabelGuides.draw_guides(self.canvas)

    def start_drag(self, event):
        """Remember where the mouse started."""

        self.drag_start_x = event.x
        self.drag_start_y = event.y


    def drag_image(self, event):
        """Drag the label."""

        dx = event.x - self.drag_start_x
        dy = event.y - self.drag_start_y

        self.canvas.move("label", dx, dy)

        self.image_x += dx
        self.image_y += dy

        self.drag_start_x = event.x
        self.drag_start_y = event.y
        print("Dragging...")