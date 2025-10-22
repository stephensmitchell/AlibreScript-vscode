"""Auto-generated Python 3 stub file for AlibreScript API

This file provides type hints and documentation for the AlibreScript API.
Compatible with Python 3.6+ and modern IDEs with type checking support.
"""

from typing import Any, List


class TwoD:

    def GetPerpendicularVector(self, Vector: List) -> List[float]:
        """Gets a vector that is perpendicular to a vector
        
        Args:
            Vector: Vector [X, Y]
        
        Returns:
            Vector that is perpendicular [X, Y]
        """
        ...

    def NormalizeVector(self, Vector: List) -> List[float]:
        """Normalizes a vector
        
        Args:
            Vector: Vector [X, Y]
        
        Returns:
            Normalized vector [X, Y]
        """
        ...

    def RotatePoint(self, Point: List, Angle: float) -> List[float]:
        """Rotates a point
        
        Args:
            Point: Point to rotate as [X, Y]
            Angle: Angle to rotate in degrees
        
        Returns:
            Rotated point as [RX, RY]
        """
        ...
