"""
Record Label Composer

print_layout.py

Page layout calculations.
"""


class PrintLayout:
    """Page layout calculations."""

    TEMPLATE_LEFT_MM = 12
    TEMPLATE_TOP_MM = 20.0

    # A4 paper size
    PAGE_WIDTH_MM = 210.0
    PAGE_HEIGHT_MM = 297.0

    # Label size
    LABEL_DIAMETER_MM = 100.0 
    # Label centres (millimetres)

    HORIZONTAL_PITCH_MM = 99.0
    VERTICAL_PITCH_MM = 99.0

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

    @staticmethod
    def get_label_centres_mm():
        """Return the four label centres in millimetres."""

        return (
        (60.0, 125.0),   # Circle 1
        (151.0, 72.0),   # Circle 2
        (60.0, 235.0),   # Circle 3
        (151.0, 182.0),  # Circle 4
    )