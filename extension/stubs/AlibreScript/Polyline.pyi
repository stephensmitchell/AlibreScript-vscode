"""Auto-generated Python 3 stub file for AlibreScript API

This file provides type hints and documentation for the AlibreScript API.
Compatible with Python 3.6+ and modern IDEs with type checking support.
"""

from typing import Any
from typing import overload


class Polyline:

    def AddArc(self, Center: PolylinePoint, Start: PolylinePoint, End: PolylinePoint, MinimumSegments: int) -> Any:
        """Adds an arc to the polyline. The arc is approcimated with straight line segments
        
        Args:
            Center: Point defining center of arc
            Start: Point defining start of arc
            End: Point defining end of arc
            MinimumSegments: Minimum number of line segments to use to form arc
        """
        ...

    def AddCircle(self, CenterX: float, CenterY: float, Diameter: float, sides: int) -> Any:
        """Adds a circle to the line
        
        Args:
            CenterX: X coordinate of circle center
            CenterY: Y coordinate of circle center
            Diameter: Diameter of circle
            sides: Number of sides to use to approximate circle
        """
        ...

    def AddPoint(self, Point: PolylinePoint) -> Point:
        """Adds a new point to the polyline
        
        Args:
            Point: Point to add
        """
        ...

    def AddPolyline(self, AppendLine: Polyline) -> Any:
        """Appends a line to the current line
        
        Args:
            AppendLine: Line to append
        """
        ...

    @overload
    def Clone(self) -> Any:
        """Creates an exact copy of the line
        
        Returns:
            Copy of line
        """
        ...

    @overload
    def Clone(self, StartIndex: int, EndIndex: int) -> Any:
        """Creates an exact copy of a section of the line
        
        Args:
            StartIndex: 0-based index of first point to include in copy
            EndIndex: 0-based index of last point to include in copy
        
        Returns:
            Copied line
        """
        ...

    @overload
    def FindIntersection(self, L1: Polyline, L2: Polyline) -> Any:
        """Finds the first intersection point between two lines
        
        Args:
            L1: First line
            L2: Second line
        
        Returns:
            First intersection point or null if none found
        """
        ...

    @overload
    def FindIntersection(self, A1: PolylinePoint, A2: PolylinePoint, B1: PolylinePoint, B2: PolylinePoint) -> Any:
        """Gets the intersection between the line segments A1A2 and B1B2
        
        Args:
            A1: First segment start point
            A2: First segment end point
            B1: Second segment start point
            B2: Second segment end point
        
        Returns:
            Intersection point or null if not found
        """
        ...

    def FindIntersectionWithCircle(self, L1: Polyline, CircleX: float, CircleY: float, Radius: float) -> Any:
        """Finds first intersection of line with a circle
        
        Args:
            L1: Line to check
            CircleX: X-coordinate of circle center
            CircleY: Y-coordinate of circle center
            Radius: Radius of circle
        
        Returns:
            Intersection point or null if not found
        """
        ...

    def InsertPoint(self, Index: int, Point: PolylinePoint) -> None:
        """Inserts a point at a specific location
        
        Args:
            Index: 0-based index of location to insert
            Point: Point to insert
        """
        ...

    def IsPointOnLine(self, A1: PolylinePoint, A2: PolylinePoint, Point: PolylinePoint, Tolerance: float) -> bool:
        """Determines if a point is on a line segment
        
        Args:
            A1: First point of line segment
            A2: Last point of line segment
            Point: Point to check
            Tolerance: Fudge factor
        
        Returns:
            True if point is on line
        """
        ...

    def Join(self, AppendLine: Polyline) -> Any:
        """Joins a line onto the end of the current line and returns the new line
        
        Args:
            AppendLine: The line to join to the current line
        
        Returns:
            The new line created from this line plus the appended line
        """
        ...

    def Offset(self, OffsetX: float, OffsetY: float) -> Any:
        """Applies an offset to all points on the line
        
        Args:
            OffsetX: X offset to apply
            OffsetY: Y offset to apply
        """
        ...

    def RemoveDuplicates(self) -> None:
        """Removes duplicate points that are next to each other
        """
        ...

    def RotateZ(self, CenterX: float, CenterY: float, Angle: float) -> None:
        """Rotates the polyline around the Z axis
        
        Args:
            CenterX: X coordinate of center of rotation
            CenterY: Y coordinate of center of rotation
            Angle: Number of degrees to rotate
        """
        ...

    def SplitAtPoint(self, SplitPoint: PolylinePoint, Tolerence: float) -> Any:
        """Splits a polyline at a point, creating two polylines
        
        Args:
            SplitPoint: Point to split at
            Tolerence: Tolerance to determine if point is on/near line
        
        Returns:
            List of polylines [A, B]
        """
        ...
