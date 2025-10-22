"""Auto-generated Python 3 stub file for AlibreScript API

This file provides type hints and documentation for the AlibreScript API.
Compatible with Python 3.6+ and modern IDEs with type checking support.
"""

from typing import Any


class Line3D:


    def __init__(self, start_point: List, end_point: List, is_reference: bool) -> None:
        """Creates a new 3D line

        Args:
            start_point: Start point as [x, y, z]
            end_point: End point as [x, y, z]
            is_reference: True for reference geometry
        """
        ...

    # Properties (read-only attributes set by Alibre at runtime)
    End: Any  # The end point as a sketchpoint object
    EndPoint: Any  # The end point of the line [x, y, z]
    IsReference: Any  # True if the line is a reference line, false if it is a regular line
    Length: Any  # The length of the line in script units
    Start: Any  # The start point as a sketchpoint object
    StartPoint: Any  # The start point of the line [x, y, z]

    pass
