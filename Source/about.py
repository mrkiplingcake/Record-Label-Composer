"""
Record Label Composer
Build 002 - Workbench

about.py
About dialog for the application.
"""

import tkinter as tk
from tkinter import messagebox

from version import about_text


def show_about(parent=None):
    """Display the About dialog."""
    messagebox.showinfo(
        title="About Record Label Composer",
        message=about_text(),
        parent=parent,
    )


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    show_about(root)
