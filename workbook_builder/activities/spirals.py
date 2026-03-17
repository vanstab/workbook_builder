"""Spiral tracing activity."""

import math
from ..colors import C, get_accent
from ..icons import draw_star
from .base import Activity, WIDTH, HEIGHT


class Spirals(Activity):
    name = "spirals"
    title = "Trace the Spirals"
    instruction = "Follow the spiral from outside to the star in the middle!"

    def draw_content(self, canvas, page_idx, theme, layout):
        spiral_data = [
            (WIDTH / 2 - 140, HEIGHT - 280, 90),
            (WIDTH / 2 + 140, HEIGHT - 280, 90),
            (WIDTH / 2, HEIGHT - 540, 110),
        ]

        for i, (cx, cy, max_r) in enumerate(spiral_data):
            col = get_accent(page_idx, i, theme)
            canvas.setStrokeColor(col)
            canvas.setLineWidth(layout["thickness"] + 0.5)
            canvas.setDash(*layout["dash"])

            p = canvas.beginPath()
            first = True
            for j in range(0, 900, 3):
                rad = math.radians(j)
                r = max_r - j * (max_r - 8) / 900
                if r < 5:
                    break
                x = cx + r * math.cos(rad)
                yp = cy + r * math.sin(rad)
                if first:
                    p.moveTo(x, yp)
                    first = False
                else:
                    p.lineTo(x, yp)
            canvas.drawPath(p, fill=0)
            canvas.setDash()

            draw_star(canvas, cx, cy, 0.8)

            canvas.setFillColor(col)
            canvas.setFont("Helvetica-Bold", 11)
            canvas.drawString(cx + max_r + 5, cy - 5, "start")
