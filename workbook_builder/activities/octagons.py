"""Octagon tracing activity."""

from ..icons import draw_flower
from .polygon_base import RegularPolygonActivity


class Octagons(RegularPolygonActivity):
    """Octagon (8-sided polygon) tracing activity."""

    sides = 8
    name = "octagons"
    title = "Trace the Octagons"
    instruction = "Follow the dotted lines to trace each octagon!"
    icon_function = draw_flower
