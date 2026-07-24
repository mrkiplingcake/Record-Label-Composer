"""
Record Label Composer

geometry.py

Geometry helper functions used throughout the application.
"""

from constants import WORKING_DIAMETER_MM


class LabelGeometry:
    """Geometry calculations for the workspace."""

    @staticmethod
    def get_working_diameter_pixels(canvas):
        """Returns the working radius of the label."""
        width = canvas.winfo_width()
        height = canvas.winfo_height()

        return min(width, height) * 0.76

    @staticmethod
    def get_working_radius_pixels(canvas):
        """Returns the working radius in pixels."""
        return LabelGeometry.get_working_diameter_pixels(canvas) / 2