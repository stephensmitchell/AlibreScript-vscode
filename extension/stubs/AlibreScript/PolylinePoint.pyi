"""Auto-generated Python 3 stub file for AlibreScript API

This file provides type hints and documentation for the AlibreScript API.
Compatible with Python 3.6+ and modern IDEs with type checking support.
"""

from typing import Any


class PolylinePoint:

    def Offset(self, X: float, Y: float) -> Any:
        """Applies an offset to the point and creates a new point
        
        Args:
            X: X offset to apply
            Y: Y offset to apply
        
        Returns:
            New point with offset applied
        """
        ...

    def RotateZ(self, CenterX: float, CenterY: float, Angle: float) -> None:
        """Rotates the point around the Z axis
        
        Args:
            CenterX: X coordinate of center of rotation
            CenterY: Y coordinate of center of rotation
            Angle: Number of degrees to rotate
        """
        ...

    def Scale(self, ScaleOriginX: float, ScaleOriginY: float, ScaleFactor: float) -> Any:
        """Scales the point location based on an origin for the scaling
        
        Args:
            ScaleOriginX: X-coordinate for scaling origin
            ScaleOriginY: Y-coordinate for scaling origin
            ScaleFactor: Factor for scaling as a percentage
        
        Returns:
            New point with scaling applied
        """
        ...

    # Enums and Constants
    class Constants:
        """Class constants"""
        X: Any = ...  # X coordinate
        Y: Any = ...  # Y coordinate
