"""Auto-generated Python 3 stub file for AlibreScript API

This file provides type hints and documentation for the AlibreScript API.
Compatible with Python 3.6+ and modern IDEs with type checking support.
"""

from typing import Any


class EllipticalArc:


    def __init__(self, center: List, start: List, end: List, major_radius: float, major_axis_angle: float, minor_major_ratio: float, is_reference: bool) -> None:
        """Creates an elliptical arc

        Args:
            center: Center point as [x, y]
            start: Start point as [x, y]
            end: End point as [x, y]
            major_radius: Major radius of ellipse
            major_axis_angle: Angle of major axis in degrees
            minor_major_ratio: Ratio of minor to major radius
            is_reference: True for reference geometry
        """
        ...

    # Properties (read-only attributes set by Alibre at runtime)
    Center: Any  # The center of the elliptical arc [x, y]
    CenterPoint: Any  # The center point as a sketchpoint object
    End: Any  # The end point as a sketchpoint object
    EndPoint: Any  # The end point of the arc [x, y]
    IsReference: Any  # True if the elliptical arc is a reference elliptical arc, false if it is a regular elliptical arc
    MajorAxisAngle: Any  # Angle of major axis
    MinorMajorRatio: Any  # Ratio of minor radius to major radius
    Radius: Any  # Radius on major axis
    Start: Any  # The start point as a sketchpoint object
    StartPoint: Any  # The start point of the arc [x, y]

    pass
