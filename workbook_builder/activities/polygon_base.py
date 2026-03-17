"""Base class for regular polygon tracing activities."""

import math
from ..colors import get_accent
from .base import Activity, WIDTH, HEIGHT


class RegularPolygonActivity(Activity):
    """Base class for regular polygon tracing (pentagon, hexagon, octagon, etc.).

    Subclasses must define:
    - sides: int (number of sides, e.g., 5 for pentagon, 6 for hexagon)
    - name: str (activity identifier)
    - title: str (display title)
    - instruction: str (user instruction)
    - icon_function: function to draw icon in center
    """

    sides = 5  # Override in subclasses
    icon_function = None  # Override in subclasses

    def draw_content(self, canvas, page_idx, theme, layout):
        """Draw regular polygons in a 3x2 grid."""
        # Standard 6-position grid for shapes
        positions = [
            (150, HEIGHT - 235, 60),
            (WIDTH / 2, HEIGHT - 235, 60),
            (WIDTH - 150, HEIGHT - 235, 60),
            (150, HEIGHT - 445, 70),
            (WIDTH / 2, HEIGHT - 445, 70),
            (WIDTH - 150, HEIGHT - 445, 70),
        ]

        for i, (cx, cy, r) in enumerate(positions):
            self._draw_polygon(canvas, cx, cy, r, i, page_idx, theme, layout)

    def _draw_polygon(self, canvas, cx, cy, r, idx, page_idx, theme, layout):
        """Draw a single regular polygon.

        Args:
            canvas: reportlab Canvas
            cx, cy: center position
            r: radius (distance from center to vertex)
            idx: position index (for color selection)
            page_idx: page index (for color selection)
            theme: theme dictionary
            layout: layout configuration
        """
        # Set stroke style
        col = get_accent(page_idx, idx, theme)
        canvas.setStrokeColor(col)
        canvas.setLineWidth(layout["thickness"] + 0.5)
        canvas.setDash(*layout["dash"])

        # Calculate polygon vertices
        angle_step = 360 / self.sides
        points = []
        for j in range(self.sides):
            angle = (j * angle_step - 90) * math.pi / 180
            x = cx + r * math.cos(angle)
            y = cy + r * math.sin(angle)
            points.append((x, y))

        # Draw polygon path
        p = canvas.beginPath()
        p.moveTo(points[0][0], points[0][1])
        for x, y in points[1:]:
            p.lineTo(x, y)
        p.close()
        canvas.drawPath(p, fill=0, stroke=1)
        canvas.setDash()

        # Draw icon in center (icon functions take canvas, cx, cy, scale)
        if self.icon_function is not None:
            icon_scale = r * 0.018
            # Call as class attribute to avoid method binding issues
            self.__class__.icon_function(canvas, cx, cy, icon_scale)
