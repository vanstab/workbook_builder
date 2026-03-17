"""Hexagon tracing activity."""

from ..icons import draw_heart
from .polygon_base import RegularPolygonActivity


class Hexagons(RegularPolygonActivity):
    """Hexagon (6-sided polygon) tracing activity."""

    sides = 6
    name = "hexagons"
    title = "Trace the Hexagons"
    instruction = "Follow the dotted lines to trace each hexagon!"
    icon_function = draw_heart
