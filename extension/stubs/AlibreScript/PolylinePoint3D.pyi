"""Auto-generated Python 3 stub file for AlibreScript API

This file provides type hints and documentation for the AlibreScript API.
Compatible with Python 3.6+ and modern IDEs with type checking support.
"""

from typing import Any


class PolylinePoint3D:

    def Offset(self, X: float, Y: float, Z: float) -> Any:
        """Applies an offset to the point and creates a new point
        
        Args:
            X: X offset to apply
            Y: Y offset to apply
            Z: Z offset to apply
        
        Returns:
            New point with offset applied
        """
        ...

    def Scale(self, ScaleOriginX: float, ScaleOriginY: float, ScaleOriginZ: float, ScaleFactor: float) -> Any:
        """Scales the point location based on an origin for the scaling
        
        Args:
            ScaleOriginX: X-coordinate for scaling origin
            ScaleOriginY: Y-coordinate for scaling origin
            ScaleOriginZ: Z-coordinate for scaling origin
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
        Z: Any = ...  # Z coordinate
