"""
Record Label Composer

print_layout.py

Page layout calculations.
"""


class PrintLayout:
    """Page layout calculations."""

    # A4 paper size
    PAGE_WIDTH_MM = 210
    PAGE_HEIGHT_MM = 297
    LABEL_DIAMETER_MM = 100

    @staticmethod
    def get_page_size_mm():
        """Return the page size in millimetres."""
        return (
            PrintLayout.PAGE_WIDTH_MM,
            PrintLayout.PAGE_HEIGHT_MM,
        )

    @staticmethod
    def get_page_centre_mm():
        """Return the centre of the page."""
        return (
            PrintLayout.PAGE_WIDTH_MM / 2,
            PrintLayout.PAGE_HEIGHT_MM / 2,
        )