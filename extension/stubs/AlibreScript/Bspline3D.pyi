"""Auto-generated Python 3 stub file for AlibreScript API

This file provides type hints and documentation for the AlibreScript API.
Compatible with Python 3.6+ and modern IDEs with type checking support.
"""

from typing import Any


class Bspline3D:


    def __init__(self, order: int, control_points: List, knot_vectors: List, weights: List, is_reference: bool) -> None:
        """Creates a 3D bspline

        Args:
            order: Order of the bspline
            control_points: Control points as list of [x, y, z]
            knot_vectors: Knot vectors
            weights: Weights for each control point
            is_reference: True for reference geometry
        """
        ...

    # Properties (read-only attributes set by Alibre at runtime)
    ControlPoints: Any  # The control points [x1, y1, ..., xn, yn]
    IsReference: Any  # True if the bspline is a reference bspline, false if it is a regular bspline
    KnotVectors: Any  # The knot vectors [k1, k2, ..., kn]
    Length: Any  # Gets the length of the Bspline
    Order: Any  # The order of the bspline
    Weights: Any  # The weights [w1, w2, ..., wn]

    def GetNormalAt(self, u: float) -> List[float]:
        """Gets the normal vector at a point on the spline
        
        Args:
            u: Location along the spline. 0.0 = start, 1.0 = end
        
        Returns:
            Vector for point on the spline at the specified location (A, B, C)
        """
        ...

    def GetPointAt(self, u: float) -> List[float]:
        """Gets a point on the spline
        
        Args:
            u: Location along the spline. 0.0 = start, 1.0 = end
        
        Returns:
            Point on the spline at the specified location [X, Y, Z]
        """
        ...

    def GetX(self, u: float) -> float:
        """Gets the X value of the spline at a location along the spline
        
        Args:
            u: Location along the spline. 0.0 = start, 1.0 = end
        
        Returns:
            X value of spline at the specified location
        """
        ...

    def GetY(self, u: float) -> float:
        """Gets the Y value of the spline at a location along the spline
        
        Args:
            u: Location along the spline. 0.0 = start, 1.0 = end
        
        Returns:
            Y value of spline at the specified location
        """
        ...

    def GetZ(self, u: float) -> float:
        """Gets the Z value of the spline at a location along the spline
        
        Args:
            u: Location along the spline. 0.0 = start, 1.0 = end
        
        Returns:
            Y value of spline at the specified location
        """
        ...

    def Subdivide(self, Segments: int) -> Any:
        """Divides the Bspline up into segments
        
        Args:
            Segments: Number of segments to obtain
        
        Returns:
            List of points between segments [X1, Y1, Z1, X2, Y2, Z2, ...]
        """
        ...

    def SubdivideGetNormals(self, Segments: int) -> Any:
        """Divides the Bspline up into segments and gets the normal for each point
        
        Args:
            Segments: Number of segments to obtain
        
        Returns:
            List of points between segments and normals [X1, Y1, Z1, A1, B1, C1, X2, Y2, Z2, A2, B2, C2, ...]
        """
        ...
