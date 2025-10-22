"""Auto-generated Python 3 stub file for AlibreScript API

This file provides type hints and documentation for the AlibreScript API.
Compatible with Python 3.6+ and modern IDEs with type checking support.
"""

from typing import Any, List
from typing import overload


if TYPE_CHECKING:
    from AlibreScript.Assembly import Assembly
    from AlibreScript.Part import Part


class Sketch3D:

    # Properties (read-only attributes set by Alibre at runtime)
    Figures: Any  # A list of figures defines on the sketch, e.g. bspline
    Name: Any  # Name of the sketch

    def AddArc(self, NewArc: CircularArc3D) -> Any:
        """Adds a circular arc to the sketch
        
        Args:
            NewArc: Arc to add
        """
        ...

    def AddArcCenterStartEnd(self, CenterX: float, CenterY: float, CenterZ: float, StartX: float, StartY: float, StartZ: float, EndX: float, EndY: float, EndZ: float) -> Any:
        """Adds a circular arc using three points - center, start and end
            Arc goes anti-clockwise from start to end
        
        Args:
            CenterX: X coordinate for center
            CenterY: Y coordinate for center
            CenterZ: Z coordinate for center
            StartX: X coordinate for start
            StartY: Y coordinate for start
            StartZ: Z coordinate for start
            EndX: X coordinate for end
            EndY: Y cordinate for end
            EndZ: Z coordnate for end
        """
        ...

    @overload
    def AddBspline(self, Points: List) -> Any:
        """Adds a Bspline to the sketch
        
        Args:
            Points: List of control points [X1, Y1, Z1, X2, Y2, Z2, ...]
        
        Returns:
            The Bspline object that was created
        """
        ...

    @overload
    def AddBspline(self, Bspline: Bspline3D) -> Any:
        """Adds a Bspline to the sketch
        
        Args:
            Bspline: Bspline to add
        """
        ...

    @overload
    def AddLine(self, StartPoint: List, EndPoint: List) -> Any:
        """Adds a line to the sketch
        
        Args:
            StartPoint: Start of line [X, Y, Z]
            EndPoint: End of line [X, Y, Z]
        """
        ...

    @overload
    def AddLine(self, NewLine: Line3D) -> Any:
        """Adds a line to the sketch
        
        Args:
            NewLine: 3D line to add
        """
        ...

    @overload
    def AddLine(self, X1: float, Y1: float, Z1: float, X2: float, Y2: float, Z2: float) -> Any:
        """Adds a line to the sketch
        
        Args:
            X1: Start point X
            Y1: Start point Y
            Z1: Start point Z
            X2: End point X
            Y2: End point Y
            Z2: End point Z
        """
        ...

    def AddLines(self, Points: List) -> Any:
        """Adds a polyline to the sketch
        
        Args:
            Points: Set of points [Point1X, Point1Y, Point1Z, Point2X, Point2Y, Point2Z, ...]
        """
        ...

    @overload
    def AddPoint(self, X: float, Y: float, Z: float) -> Point:
        """Adds a point to the sketch
        
        Args:
            X: Point X coordinate
            Y: Point Y coordinate
            Z: Point Z coordinate
        """
        ...

    @overload
    def AddPoint(self, NewPoint: SketchPoint3D) -> Point:
        """Adds a point to the sketch
        
        Args:
            NewPoint: Point to add
        """
        ...

    def AddPolyline(self, Line: Polyline3D) -> Any:
        """Adds a polyline to the sketch
        
        Args:
            Line: Polyine to add
        """
        ...

    def FromXml(self, Xml: str) -> Any:
        """Adds elements to the sketch from XML
        
        Args:
            Xml: XML to parse
        """
        ...

    def GetPart(self) -> Part:
        """Part that the sketch is defined on
        
        Returns:
            Part
        """
        ...

    def GetSelectionAssembly(self) -> Assembly:
        """The assembly that the edge was selected on
            Only valid when a selection has been made
        
        Returns:
            Assembly or null for no assembly
        """
        ...

    def LoadXml(self, FileName: str) -> None:
        """Loads the sketch from an XML file
        
        Args:
            FileName: Path and name of file to load from
        """
        ...

    def SavetoXml(self, FileName: str) -> None:
        """Saves the sketch to an XML file
        
        Args:
            FileName: Path and name of file to save to
        """
        ...

    def ToXml(self) -> str:
        """Saves the sketch to an XML string
        
        Returns:
            XML string representing sketch
        """
        ...
