"""Zigzag line tracing activity."""

from ..colors import C
from .base import Activity


class ZigzagLines(Activity):
    name = "zigzag"
    title = "Zigzag Lines"
    instruction = "Trace the zigzag path from left to right!"

    def effective_rows(self, layout):
        return min(layout["rows"], 5)

    def draw_content(self, canvas, page_idx, theme, layout):
        starts = theme["start_icons"]
        ends = theme["end_icons"]
        spacing = self.row_spacing(layout)

        for i in range(self.effective_rows(layout)):
            ly = self.content_top() - 5 - i * spacing
            starts[i % len(starts)](canvas, 80, ly)

            canvas.setStrokeColor(C["gray"])
            canvas.setLineWidth(layout["thickness"])
            canvas.setDash(*layout["dash"])

            p = canvas.beginPath()
            zx = 115
            p.moveTo(zx, ly)
            seg_w = 28
            zig_h = min(22, spacing * 0.2)
            for j in range(12):
                zx += seg_w
                zy = ly + zig_h if j % 2 == 0 else ly - zig_h
                p.lineTo(zx, zy)
            canvas.drawPath(p, fill=0)
            canvas.setDash()

            ends[i % len(ends)](canvas, self.end_x(), ly)
