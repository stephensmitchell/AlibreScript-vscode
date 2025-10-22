"""Auto-generated Python 3 stub file for AlibreScript API

This file provides type hints and documentation for the AlibreScript API.
Compatible with Python 3.6+ and modern IDEs with type checking support.
"""

from typing import Any


class Circle:


    def __init__(self, center: List, radius: float, is_reference: bool) -> None:
        """Creates a 2D circle which can be added to sketches

        Args:
            center: Center point as [x, y]
            radius: Circle radius
            is_reference: True for reference geometry
        """
        ...

    # Properties (read-only attributes set by Alibre at runtime)
    Center: Any  # The center of the circle [x, y]
    CenterPoint: Any  # The center of the circle as a sketch point
    IsReference: Any  # True if the circle is a reference circle, false if it is a regular circle
    Length: Any  # The length of the circle circumference in script units
    Radius: Any  # Radius of the circle

    pass
