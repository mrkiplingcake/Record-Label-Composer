"""
Record Label Composer

panels.py
Creates the 2x2 artwork panel grid.
"""

from artwork_panel import ArtworkPanel


def create_panel_grid(master):

    panels = []

    for row in range(2):
        master.grid_rowconfigure(row, weight=1)

        for col in range(2):
            master.grid_columnconfigure(col, weight=1)

            number = row * 2 + col + 1

            panel = ArtworkPanel(master, number)

            panel.grid(
                row=row,
                column=col,
                padx=10,
                pady=10,
                sticky="nsew",
            )

            panels.append(panel)

    return panels