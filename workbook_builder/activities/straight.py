"""Straight line tracing activity."""

from ..colors import C
from .base import Activity


class StraightLines(Activity):
    name = "straight"
    title = "Straight Lines"
    instruction = "Trace the dotted lines from left to right!"

    def draw_content(self, canvas, page_idx, theme, layout):
        starts = theme["start_icons"]
        ends = theme["end_icons"]
        spacing = self.row_spacing(layout)

        for i in range(self.effective_rows(layout)):
            ly = self.content_top() - i * spacing
            starts[i % len(starts)](canvas, self.start_x(), ly)
            canvas.setStrokeColor(C["gray"])
            canvas.setLineWidth(layout["thickness"])
            canvas.setDash(*layout["dash"])
            canvas.line(self.line_start(), ly, self.line_end(), ly)
            canvas.setDash()
            ends[i % len(ends)](canvas, self.end_x(), ly)
