"""Activity registry - imports all activities and builds the registry."""

from .straight import StraightLines
from .wavy import WavyLines
from .zigzag import ZigzagLines
from .diagonals import DiagonalLines
from .waves import Waves
from .loops import Loops
from .circles import Circles
from .squares import Squares
from .triangles import Triangles
from .pentagons import Pentagons
from .hexagons import Hexagons
from .octagons import Octagons
from .ovals import Ovals
from .rectangles import Rectangles
from .trapezoids import Trapezoids
from .diamonds import Diamonds
from .spirals import Spirals
from .addition import Addition
from .subtraction import Subtraction
from .spelling import Spelling
from .colour import Colour

# Build the activity registry
# Note: Spelling and Colour are not included here as they require parameters
# and should be created on demand.
ACTIVITY_REGISTRY = {
    "straight": StraightLines(),
    "wavy": WavyLines(),
    "zigzag": ZigzagLines(),
    "diagonals": DiagonalLines(),
    "waves": Waves(),
    "loops": Loops(),
    "circles": Circles(),
    "squares": Squares(),
    "triangles": Triangles(),
    "pentagons": Pentagons(),
    "hexagons": Hexagons(),
    "octagons": Octagons(),
    "ovals": Ovals(),
    "rectangles": Rectangles(),
    "trapezoids": Trapezoids(),
    "diamonds": Diamonds(),
    "spirals": Spirals(),
    "addition": Addition(),
    "subtraction": Subtraction(),
}

# Add spelling and colour to the list of valid activity names even though they're not in the registry
# They will be created on demand in the generator
_VALID_ACTIVITIES = list(ACTIVITY_REGISTRY.keys()) + ["spelling", "colour"]

# List of all base activities (excludes numbers and letters which are dynamic)
# Includes spelling even though it's created on demand
ALL_ACTIVITIES = _VALID_ACTIVITIES

__all__ = ["ACTIVITY_REGISTRY", "ALL_ACTIVITIES"]
