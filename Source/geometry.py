"""
Record Label Composer

geometry.py

Geometry helper functions used throughout the application.
"""

from constants import (
    LABEL_DIAMETER_MM,
    SAFE_DIAMETER_MM,
    WORKING_DIAMETER_MM,
    WORKSPACE_DIAMETER_MM,
)


class LabelGeometry:
    """Geometry calculations for the workspace."""

    @staticmethod
    def get_workspace_size_pixels(canvas):
        """Returns the usable workspace size in pixels."""
        width = canvas.winfo_width()
        height = canvas.winfo_height()

        return min(width, height)

    @staticmethod
    def get_workspace_pixels_per_mm(canvas):
         """Returns the number of pixels per millimetre in the workspace."""
         workspace = LabelGeometry.get_workspace_size_pixels(canvas)


         return workspace / WORKSPACE_DIAMETER_MM

    @staticmethod
    def get_working_diameter_pixels(canvas):
        pixels_per_mm = LabelGeometry.get_workspace_pixels_per_mm(canvas)
        return WORKING_DIAMETER_MM * pixels_per_mm

    @staticmethod
    def get_working_radius_pixels(canvas):
        """Returns the working radius in pixels."""
        return LabelGeometry.get_working_diameter_pixels(canvas) / 2

    @staticmethod
    def get_cut_radius_pixels(canvas):
        """Returns the cut radius in pixels."""
        pixels_per_mm = LabelGeometry.get_workspace_pixels_per_mm(canvas)
        return (LABEL_DIAMETER_MM * pixels_per_mm) / 2

    @staticmethod
    def get_safe_radius_pixels(canvas):
        """Returns the safe radius in pixels."""
        pixels_per_mm = LabelGeometry.get_workspace_pixels_per_mm(canvas)
        return (SAFE_DIAMETER_MM * pixels_per_mm) / 2