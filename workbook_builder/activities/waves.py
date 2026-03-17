"""Wave tracing activity."""

import math
from ..colors import C
from .base import Activity


class Waves(Activity):
    name = "waves"
    title = "Waves"
    instruction = "Trace the waves from left to right!"

    def effective_rows(self, layout):
        return min(layout["rows"], 4)

    def draw_content(self, canvas, page_idx, theme, layout):
        starts = theme["start_icons"]
        ends = theme["end_icons"]
        spacing = self.row_spacing(layout)

        for i in range(self.effective_rows(layout)):
            ly = self.content_top() - 5 - i * spacing
            starts[i % len(starts)](canvas, 70, ly)

            canvas.setStrokeColor(C["gray"])
            canvas.setLineWidth(layout["thickness"])
            canvas.setDash(*layout["dash"])

            p = canvas.beginPath()
            first = True
            loop_w = 50
            loop_h = min(28, spacing * 0.25)
            for lx in range(0, 700 + 1):
                t = lx / 100.0
                x = 115 + t * loop_w
                y = ly + loop_h * math.sin(t * 2 * math.pi)
                if x > 475:
                    break
                if first:
                    p.moveTo(x, y)
                    first = False
                else:
                    p.lineTo(x, y)
            canvas.drawPath(p, fill=0)
            canvas.setDash()

            ends[i % len(ends)](canvas, self.end_x(), ly)
