"""Auto-generated Python 3 stub file for AlibreScript API

This file provides type hints and documentation for the AlibreScript API.
Compatible with Python 3.6+ and modern IDEs with type checking support.
"""

from typing import Any


class CircularArc:


    @overload
    def __init__(self, center: List, start: List, end: List, is_reference: bool) -> None:
        """Creates an arc using the center, start point and end point

        Args:
            center: Center point as [x, y]
            start: Start point as [x, y]
            end: End point as [x, y]
            is_reference: True for reference geometry
        """
        ...

    @overload
    def __init__(self, center: List, start: List, angle: float, is_reference: bool) -> None:
        """Creates an arc using the center, start point and an angle

        Args:
            center: Center point as [x, y]
            start: Start point as [x, y]
            angle: Sweep angle in degrees
            is_reference: True for reference geometry
        """
        ...

    # Properties (read-only attributes set by Alibre at runtime)
    Angle: Any  # Angle of arc
    Center: Any  # The center of the arc [x, y]
    CenterPoint: Any  # The center point as a sketchpoint object
    End: Any  # The end point as a sketchpoint object
    EndPoint: Any  # The end point of the arc [x, y]
    IsReference: Any  # True if the arc is a reference arc, false if it is a regular arc
    Radius: Any  # Radius of arc
    Start: Any  # The start point as a sketchpoint object
    StartPoint: Any  # The start point of the arc [x, y]
    Type: Any  # Type of arc

    pass

    # Enums and Constants
    class ArcType:
        """Types of circular arcs"""
        pass
