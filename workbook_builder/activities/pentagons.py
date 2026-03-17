"""Pentagon tracing activity."""

from ..icons import draw_star
from .polygon_base import RegularPolygonActivity


class Pentagons(RegularPolygonActivity):
    """Pentagon (5-sided polygon) tracing activity."""

    sides = 5
    name = "pentagons"
    title = "Trace the Pentagons"
    instruction = "Follow the dotted lines to trace each pentagon!"
    icon_function = draw_star
