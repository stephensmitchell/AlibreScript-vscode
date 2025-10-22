"""Auto-generated Python 3 stub file for AlibreScript API

This file provides type hints and documentation for the AlibreScript API.
Compatible with Python 3.6+ and modern IDEs with type checking support.
"""

from typing import Any
from typing import overload


class Polyline3D:

    def AddPoint(self, Point: PolylinePoint3D) -> Point:
        """Adds a new point to the polyline
        
        Args:
            Point: Point to add
        """
        ...

    def AddPolyline(self, AppendLine: Polyline3D) -> Any:
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

    def InsertPoint(self, Index: int, Point: PolylinePoint3D) -> None:
        """Inserts a point at a specific location
        
        Args:
            Index: 0-based index of location to insert
            Point: Point to insert
        """
        ...

    def IsPointOnLine(self, A: PolylinePoint3D, B: PolylinePoint3D, P: PolylinePoint3D, Tolerance: float) -> bool:
        """Determines if a point is on a line segment
        
        Args:
            A: First point of line segment
            B: Last point of line segment
            P: Point to check
            Tolerance: Fudge factor
        
        Returns:
            True if point is on line
        """
        ...

    def Join(self, AppendLine: Polyline3D) -> Any:
        """Joins a line onto the end of the current line and returns the new line
        
        Args:
            AppendLine: The line to join to the current line
        
        Returns:
            The new line created from this line plus the appended line
        """
        ...

    def Offset(self, OffsetX: float, OffsetY: float, OffsetZ: float) -> Any:
        """Applies an offset to all points on the line
        
        Args:
            OffsetX: X offset to apply
            OffsetY: Y offset to apply
            OffsetZ: Z offset to apply
        """
        ...

    def RemoveDuplicates(self) -> None:
        """Removes duplicate points that are next to each other
        """
        ...

    def SplitAtPoint(self, SplitPoint: PolylinePoint3D, Tolerence: float) -> Any:
        """Splits a polyline at a point, creating two polylines
        
        Args:
            SplitPoint: Point to split at
            Tolerence: Tolerance to determine if point is on/near line
        
        Returns:
            List of polylines [A, B]
        """
        ...
