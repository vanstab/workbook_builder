"""Diagonal line tracing activity."""

from ..colors import C
from ..icons import draw_star
from .base import Activity


class DiagonalLines(Activity):
    name = "diagonals"
    title = "Diagonal Lines"
    instruction = "Trace the diagonal lines from the dot to the star!"

    def effective_rows(self, layout):
        return min(layout["rows"], 5)

    def draw_content(self, canvas, page_idx, theme, layout):
        spacing = self.row_spacing(layout)

        for i in range(self.effective_rows(layout)):
            ly = self.content_top() - i * spacing
            drop = min(30, spacing * 0.3)

            if i % 2 == 0:
                x1, y1, x2, y2 = 80, ly + drop / 2, 500, ly - drop / 2
            else:
                x1, y1, x2, y2 = 80, ly - drop / 2, 500, ly + drop / 2

            # Start dot
            canvas.setFillColor(C["green"])
            canvas.circle(x1, y1, 5, fill=1, stroke=0)

            # Dashed line
            canvas.setStrokeColor(C["gray"])
            canvas.setLineWidth(layout["thickness"])
            canvas.setDash(*layout["dash"])
            canvas.line(x1, y1, x2, y2)
            canvas.setDash()

            # End star
            draw_star(canvas, x2, y2, 0.8)
