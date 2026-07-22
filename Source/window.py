"""
Record Label Composer
Build 002 - Workbench

window.py
Main application window.
"""

import tkinter as tk

from constants import (
    APP_NAME,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    MIN_WINDOW_WIDTH,
    MIN_WINDOW_HEIGHT,
    BACKGROUND_COLOUR,
    STATUS_READY,
)
from version import application_title
from panels import create_panel_grid
from about import show_about


class MainWindow:
    """Main application window."""

    def __init__(self):
        self.root = tk.Tk()

        self.root.title(application_title())
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.minsize(MIN_WINDOW_WIDTH, MIN_WINDOW_HEIGHT)
        self.root.configure(bg=BACKGROUND_COLOUR)

        self._create_menu()
        self._create_layout()
        self._create_statusbar()

    def _create_menu(self):
        menubar = tk.Menu(self.root)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(
            label="About Record Label Composer",
            command=lambda: show_about(self.root)
        )
        menubar.add_cascade(label="Help", menu=help_menu)

        self.root.config(menu=menubar)

    def _create_layout(self):
        header = tk.Label(
            self.root,
            text=APP_NAME,
            font=("Segoe UI", 18, "bold"),
            bg=BACKGROUND_COLOUR,
        )
        header.pack(pady=(12, 6))

        self.workspace = tk.Frame(
            self.root,
            bg=BACKGROUND_COLOUR,
        )
        self.workspace.pack(expand=True, fill="both", padx=12, pady=8)

        create_panel_grid(self.workspace)

    def _create_statusbar(self):
        self.status = tk.Label(
            self.root,
            text=STATUS_READY,
            anchor="w",
            relief="sunken",
            padx=8,
        )
        self.status.pack(side="bottom", fill="x")

    def run(self):
        self.root.mainloop()
