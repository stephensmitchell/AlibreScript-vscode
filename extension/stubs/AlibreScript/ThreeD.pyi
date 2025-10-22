"""Auto-generated Python 3 stub file for AlibreScript API

This file provides type hints and documentation for the AlibreScript API.
Compatible with Python 3.6+ and modern IDEs with type checking support.
"""

from typing import Any, List


class ThreeD:

    def GetPerpendicularVector(self, Vector: List) -> List[float]:
        """Gets a vector that is perpendicular to a vector
        
        Args:
            Vector: Vector [X, Y, Z]
        
        Returns:
            Vector that is perpendicular [X, Y, Z]
        """
        ...

    def TransformPointUsingVectors(self, SourceVector: List, DestinationVector: List, Point: List) -> List[float]:
        """Transforms a point based on two vectors
        
        Args:
            SourceVector: Source vector [X, Y, Z]
            DestinationVector: Destination vector [X, Y, Z]
            Point: Point to transform [X, Y, Z]
        
        Returns:
            Transformed point [X, Y, Z]
        """
        ...
