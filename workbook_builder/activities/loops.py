"""Loop tracing activity - actual loops like cursive writing practice."""

import math
from ..colors import C
from .base import Activity


class Loops(Activity):
    name = "loops"
    title = "Trace the Loops"
    instruction = "Trace the loops - great practice for cursive writing!"

    def effective_rows(self, layout):
        return min(layout["rows"], 4)

    def draw_content(self, canvas, page_idx, theme, layout):
        starts = theme["start_icons"]
        ends = theme["end_icons"]
        spacing = self.row_spacing(layout)

        for i in range(self.effective_rows(layout)):
            # Adjust baseline to prevent top cutoff - lower the position
            ly = self.content_top() - 30 - i * spacing
            starts[i % len(starts)](canvas, 70, ly)

            canvas.setStrokeColor(C["gray"])
            canvas.setLineWidth(layout["thickness"])
            canvas.setDash(*layout["dash"])

            # Draw connected loops - individual circles connected in a line
            p = canvas.beginPath()
            loop_diameter = min(45, spacing * 0.5)  # Diameter of each circular loop
            loop_spacing = 60   # Spacing between loop centers
            num_loops = 6
            lead_line = 35  # Length of starting and ending lines
            start_x = 115

            # Start with a short horizontal line
            p.moveTo(start_x, ly)
            p.lineTo(start_x + lead_line, ly)

            loops_start_x = start_x + lead_line

            for loop_idx in range(num_loops):
                # Center position for this loop - circle sits ON the baseline
                x_center = loops_start_x + loop_idx * loop_spacing
                radius = loop_diameter / 2
                y_center = ly + radius  # Center is radius above baseline so circle touches baseline

                # Magic constant for perfect circles with bezier curves
                k = 0.5522847498

                # Draw circle starting from BOTTOM (touching baseline), going clockwise
                # Bottom (start position)
                p.lineTo(x_center, ly)

                # Bottom to Right
                p.curveTo(
                    x_center + radius * k, ly,                                       # control 1
                    x_center + radius, y_center - radius * k,                        # control 2
                    x_center + radius, y_center                                      # right middle
                )

                # Right to Top
                p.curveTo(
                    x_center + radius, y_center + radius * k,                        # control 1
                    x_center + radius * k, y_center + radius,                        # control 2
                    x_center, y_center + radius                                      # top
                )

                # Top to Left
                p.curveTo(
                    x_center - radius * k, y_center + radius,                        # control 1
                    x_center - radius, y_center + radius * k,                        # control 2
                    x_center - radius, y_center                                      # left middle
                )

                # Left to Bottom (back to baseline)
                p.curveTo(
                    x_center - radius, y_center - radius * k,                        # control 1
                    x_center - radius * k, ly,                                       # control 2
                    x_center, ly                                                     # back to bottom (baseline)
                )

                # Continue to next loop (if not the last one) along baseline
                if loop_idx < num_loops - 1:
                    next_center = loops_start_x + (loop_idx + 1) * loop_spacing
                    p.lineTo(next_center, ly)

            # End with a short horizontal line
            end_x = loops_start_x + (num_loops - 1) * loop_spacing
            p.lineTo(end_x + lead_line, ly)

            canvas.drawPath(p, fill=0)
            canvas.setDash()

            ends[i % len(ends)](canvas, self.end_x(), ly)
