"""Wavy line tracing activity."""

import math
from ..colors import C
from .base import Activity


class WavyLines(Activity):
    name = "wavy"
    title = "Wavy Lines"
    instruction = "Trace the waves from left to right!"

    def draw_content(self, canvas, page_idx, theme, layout):
        starts = theme["start_icons"]
        ends = theme["end_icons"]
        spacing = self.row_spacing(layout)

        for i in range(self.effective_rows(layout)):
            ly = self.content_top() - i * spacing
            starts[i % len(starts)](canvas, 70, ly)

            canvas.setStrokeColor(C["gray"])
            canvas.setLineWidth(layout["thickness"])
            canvas.setDash(*layout["dash"])

            p = canvas.beginPath()
            first = True
            amp, freq = 18, 55
            for x in range(self.line_start(), self.line_end() + 1, 2):
                wy = ly + amp * math.sin((x - self.line_start()) * math.pi / freq)
                if first:
                    p.moveTo(x, wy)
                    first = False
                else:
                    p.lineTo(x, wy)
            canvas.drawPath(p, fill=0)
            canvas.setDash()

            ends[i % len(ends)](canvas, self.end_x(), ly)
