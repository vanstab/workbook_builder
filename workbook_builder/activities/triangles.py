"""Triangle tracing activity."""

from ..colors import get_accent
from ..icons import draw_flower
from .base import Activity, WIDTH, HEIGHT


class Triangles(Activity):
    name = "triangles"
    title = "Trace the Triangles"
    instruction = "Follow the dotted lines to trace each triangle!"

    def draw_content(self, canvas, page_idx, theme, layout):
        positions = [
            (120, HEIGHT - 250, 60),
            (WIDTH / 2, HEIGHT - 250, 60),
            (WIDTH - 120, HEIGHT - 250, 60),
            (120, HEIGHT - 500, 65),
            (WIDTH / 2, HEIGHT - 500, 65),
            (WIDTH - 120, HEIGHT - 500, 65),
        ]

        for i, (cx, cy, sz) in enumerate(positions):
            col = get_accent(page_idx, i, theme)
            canvas.setStrokeColor(col)
            canvas.setLineWidth(layout["thickness"] + 0.5)
            canvas.setDash(*layout["dash"])

            p = canvas.beginPath()
            p.moveTo(cx, cy + sz)
            p.lineTo(cx - sz, cy - sz * 0.4)
            p.lineTo(cx + sz, cy - sz * 0.4)
            p.close()
            canvas.drawPath(p, fill=0, stroke=1)
            canvas.setDash()

            draw_flower(canvas, cx, cy + sz * 0.05, sz * 0.008)
