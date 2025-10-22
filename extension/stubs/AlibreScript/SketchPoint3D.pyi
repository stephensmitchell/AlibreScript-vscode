"""Auto-generated Python 3 stub file for AlibreScript API

This file provides type hints and documentation for the AlibreScript API.
Compatible with Python 3.6+ and modern IDEs with type checking support.
"""

from typing import Any


class SketchPoint3D:


    def __init__(self, x: float, y: float, z: float, is_reference: bool) -> None:
        """Creates a new 3D sketch point which can be added to sketches

        Args:
            x: X coordinate
            y: Y coordinate
            z: Z coordinate
            is_reference: True for reference geometry
        """
        ...

    # Properties (read-only attributes set by Alibre at runtime)
    IsReference: Any  # True if the point is a reference point, false if it is a regular point
    X: Any  # X-coordinate of point
    Y: Any  # Y-coordinate of point
    Z: Any  # Z-coordinate of point

    pass
