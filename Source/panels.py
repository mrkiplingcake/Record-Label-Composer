"""
Record Label Composer
Build 002 - Workbench

panels.py
Artwork panel widgets used by the main window.
"""

import tkinter as tk

from constants import PANEL_BACKGROUND, PANEL_BORDER


class ArtworkPanel(tk.Frame):
    """A simple placeholder panel for future artwork."""

    def __init__(self, master, panel_number: int):
        super().__init__(
            master,
            bg=PANEL_BACKGROUND,
            highlightbackground=PANEL_BORDER,
            highlightthickness=1,
            bd=0,
        )

        self.panel_number = panel_number

        title = tk.Label(
            self,
            text=f"Artwork Panel {panel_number}",
            font=("Segoe UI", 11, "bold"),
            bg=PANEL_BACKGROUND,
        )
        title.pack(pady=(20, 10))

        self.preview = tk.Label(
            self,
            text="Double-click here\nto load artwork\n(Build 003)",
            justify="center",
            font=("Segoe UI", 10),
            bg=PANEL_BACKGROUND,
        )
        self.preview.pack(expand=True, fill="both", padx=20, pady=20)

        self.bind("<Double-Button-1>", self._not_yet_available)
        self.preview.bind("<Double-Button-1>", self._not_yet_available)

    def _not_yet_available(self, event=None):
        self.preview.config(
            text="Artwork loading\narrives in\nBuild 003"
        )


def create_panel_grid(master):
    """Create four artwork panels in a 2x2 grid."""
    panels = []

    for row in range(2):
        master.grid_rowconfigure(row, weight=1)
        for col in range(2):
            master.grid_columnconfigure(col, weight=1)
            number = row * 2 + col + 1
            panel = ArtworkPanel(master, number)
            panel.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
            panels.append(panel)

    return panels
