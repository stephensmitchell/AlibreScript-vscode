"""Auto-generated Python 3 stub file for AlibreScript API

This file provides type hints and documentation for the AlibreScript API.
Compatible with Python 3.6+ and modern IDEs with type checking support.
"""

from typing import Any, List
from typing import overload


if TYPE_CHECKING:
    from AlibreScript.Assembly import Assembly
    from AlibreScript.Part import Part


class Sketch:

    # Properties (read-only attributes set by Alibre at runtime)
    Figures: Any  # A list of figures (line, circle, circulararc, bspline, ellipse, elliptical arc) defined on the sketch
    Name: Any  # Name of the sketch
    Origin: Any  # The point that defines the origin

    def AddArc(self, NewArc: CircularArc) -> Any:
        """Adds a circular arc to the sketch
        
        Args:
            NewArc: Arc to add
        
        Returns:
            The added circular arc
        """
        ...

    def AddArcCenterStartAngle(self, CenterX: float, CenterY: float, StartX: float, StartY: float, Angle: float, IsReference: bool = False) -> Any:
        """Adds a circular arc using center, start and angle
            Arc goes anti-clockwise from start
        
        Args:
            CenterX: X coordinate for center
            CenterY: Y coordinate for center
            StartX: X coordinate for start
            StartY: Y coordinate for start
            Angle: Arc angle in degrees
            IsReference: True if arc is a reference figure
        
        Returns:
            The added circular arc
        """
        ...

    def AddArcCenterStartEnd(self, CenterX: float, CenterY: float, StartX: float, StartY: float, EndX: float, EndY: float, IsReference: bool = False) -> Any:
        """Adds a circular arc using three points - center, start and end
            Arc goes anti-clockwise from start to end
        
        Args:
            CenterX: X coordinate for center
            CenterY: Y coordinate for center
            StartX: X coordinate for start
            StartY: Y coordinate for start
            EndX: X coordinate for end
            EndY: Y cordinate for end
            IsReference: True if arc is a reference figure
        
        Returns:
            The added circular arc
        """
        ...

    @overload
    def AddBspline(self, Order: int, ControlPoints: List, KnotVectors: List, Weights: List, IsReference: bool = False) -> Any:
        """Adds a Bspline to the sketch
        
        Args:
            Order: Order of the Bspline (Degree - 1)
            ControlPoints: List of control points
            KnotVectors: List of knot vectors
            Weights: List of control point weights
            IsReference: True to create a reference (default: False) bspline
        
        Returns:
            The created Bspline
        """
        ...

    @overload
    def AddBspline(self, Points: List, IsReference: bool = False) -> Any:
        """Adds a Bspline to the sketch through a set of points
        
        Args:
            Points: List of points
            IsReference: True to create a reference (default: False) bspline
        
        Returns:
            The created Bspline
        """
        ...

    @overload
    def AddBspline(self, NewBspline: Bspline) -> Any:
        """Adds a new bspline to the sketch
        
        Args:
            NewBspline: Bspline to add to the sketch
        
        Returns:
            The added Bspline
        """
        ...

    @overload
    def AddCircle(self, CenterX: float, CenterY: float, Diameter: float, IsReference: bool = False) -> Any:
        """Adds a circle to the sketch

        Args:
            CenterX: X coordinate of circle center
            CenterY: Y coordinate of circle center
            Diameter: Circle diameter
            IsReference: True to create a reference circle (default: False)

        Returns:
            A circle object
        """
        ...

    @overload
    def AddCircle(self, NewCircle: Circle) -> Any:
        """Adds a circle to the sketch
        
        Args:
            NewCircle: Circle to add to sketch
        
        Returns:
            The added circle
        """
        ...

    @overload
    def AddConstraint(self, Figure: ISketchFigure, Constraint: Constraints) -> Any:
        """Adds a constraint to the sketch
        
        Args:
            Figure: Figure to constrain (e.g. Line)
            Constraint: Constraint to apply
        
        Returns:
            True if constraint was added
        """
        ...

    @overload
    def AddConstraint(self, Figures: List, Constraint: Constraints) -> Any:
        """Adds a constraint to the sketch
        
        Args:
            Figures: List of Sketch figures to constrain [Figure1, Figure2, ...] (Circle, Line, CircularArc, etc.)
            Constraint: Constraint to apply
        
        Returns:
            Returns True if constraint was added
        """
        ...

    @overload
    def AddDimension(self, P1: SketchPoint, P2: SketchPoint) -> Any:
        """Adds a dimension to the sketch between two points
        
        Args:
            P1: First point
            P2: Second point
        """
        ...

    @overload
    def AddDimension(self, Circle: Circle) -> Any:
        """Adds a dimension to the radius of a circle
        
        Args:
            Circle: Circle to dimension
        """
        ...

    @overload
    def AddDimension(self, Arc: CircularArc) -> Any:
        """Adds a dimension to the radius of an arc
        
        Args:
            Arc: Arc to dimension
        """
        ...

    @overload
    def AddEllipse(self, CenterX: float, CenterY: float, MajorX: float, MajorY: float, MinorX: float, MinorY: float, IsReference: bool = False) -> Any:
        """Adds an ellipse to the sketch using three points
        
        Args:
            CenterX: X coordinate of ellipse center
            CenterY: Y coordinate of ellipse center
            MajorX: X coordinate of ellipse on major axis
            MajorY: Y coordinate of ellipse on major axis
            MinorX: X coordinate of ellipse on minor axis
            MinorY: Y coordinate of ellipse on minor axis
            IsReference: True to create a reference (default: False) ellipse
        
        Returns:
            An ellipse object
        """
        ...

    @overload
    def AddEllipse(self, CenterX: float, CenterY: float, MajorAxisDiameter: float, MinorMajorRatio: float, MajorAxisAngle: float, IsReference: bool = False) -> Any:
        """Adds an ellipse to the sketch
        
        Args:
            CenterX: X coordinate of ellipse center
            CenterY: Y coordinate of ellipse center
            MajorAxisDiameter: Diameter of ellipse on major axis
            MinorMajorRatio: Ratio of minor diameter to major diameter
            MajorAxisAngle: Angle of major axis
            IsReference: True to create a reference (default: False) ellipse
        
        Returns:
            An ellipse object
        """
        ...

    @overload
    def AddEllipse(self, NewEllipse: Ellipse) -> Any:
        """Adds an ellipse to the sketch
        
        Args:
            NewEllipse: Ellipse to add
        
        Returns:
            Added ellipse
        """
        ...

    @overload
    def AddEllipticalArc(self, CenterX: float, CenterY: float, StartX: float, StartY: float, EndX: float, EndY: float, MajorAxisDiameter: float, MinorMajorRatio: float, MajorAxisAngle: float, IsReference: bool = False) -> Any:
        """Adds an elliptical arc to the sketch
        
        Args:
            CenterX: X coordinate of arc center
            CenterY: Y coordinate of arc center
            StartX: X coorindate of arc start
            StartY: Y coordinate of arc start
            EndX: X coordinate of arc end
            EndY: Y coordinate of arc end
            MajorAxisDiameter: Diameter of ellipse on major axis
            MinorMajorRatio: Ratio of minor diameter to major diameter
            MajorAxisAngle: Angle of major axis
            IsReference: True to create a reference (default: False) elliptical arc
        
        Returns:
            An elliptical arc object
        """
        ...

    @overload
    def AddEllipticalArc(self, NewEllipticalArc: EllipticalArc) -> Any:
        """Adds an elliptical arc to the sketch
        
        Args:
            NewEllipticalArc: Elliptical arc to add
        
        Returns:
            Added elliptical arc
        """
        ...

    def AddFigure(self, NewFigure: ISketchFigure) -> Any:
        """Adds a figure to the sketch
        
        Args:
            NewFigure: Figure to add
        
        Returns:
            The added figure
        """
        ...

    @overload
    def AddLine(self, StartPoint: List, EndPoint: List, IsReference: bool = False) -> Any:
        """Adds a line to the sketch
        
        Args:
            StartPoint: Start of line [X, Y]
            EndPoint: End of line [X, Y]
            IsReference: true if line is a reference line
        
        Returns:
            The added line
        """
        ...

    @overload
    def AddLine(self, NewLine: Line) -> Any:
        """Adds a line to the sketch
        
        Args:
            NewLine: 2D line to add
        
        Returns:
            The added line
        """
        ...

    @overload
    def AddLine(self, X1: float, Y1: float, X2: float, Y2: float, IsReference: bool = False) -> Any:
        """Adds a line to the sketch
        
        Args:
            X1: Start point X
            Y1: Start point Y
            X2: End point X
            Y2: End point Y
            IsReference: true to create a reference line
        
        Returns:
            The added line
        """
        ...

    def AddLines(self, Points: List, IsReference: bool = False) -> Any:
        """Adds a polyline to the sketch
        
        Args:
            Points: Set of points [Point1X, Point1Y, Point2X, Point2Y, ...]
            IsReference: true if line is a reference line
        """
        ...

    @overload
    def AddPoint(self, X: float, Y: float) -> Point:
        """Adds a point to the sketch
        
        Args:
            X: Point X coordinate
            Y: Point Y coordinate
        
        Returns:
            The created sketch point
        """
        ...

    @overload
    def AddPoint(self, X: float, Y: float, IsReference: bool = False) -> Point:
        """Adds a point to the sketch [DEPRECATED - DO NOT USE]
        
        Args:
            X: Point X coordinate
            Y: Point Y coordinate
            IsReference: Set to false
        
        Returns:
            The added point
        """
        ...

    @overload
    def AddPoint(self, NewPoint: SketchPoint) -> Point:
        """Adds a point to the sketch
        
        Args:
            NewPoint: Point to add
        
        Returns:
            The added point
        """
        ...

    def AddPolygon(self, CenterX: float, CenterY: float, Diameter: float, Sides: int, IsReference: bool = False) -> Any:
        """Adds a regular polygon to the sketch
        
        Args:
            CenterX: X coordinate for polygon center
            CenterY: Y coordinate for polygon center
            Diameter: Diameter of polygon
            Sides: Number of sides
            IsReference: True to create a reference (default: False) polygon
        """
        ...

    def AddPolyhole(self, CenterX: float, CenterY: float, Diameter: float, IsReference: bool = False) -> Any:
        """Adds a polyhole to the sketch
            Create a "circle" whose size should be accurate regardless of the 3D printing method
            See: http://hydraraptor.blogspot.co.uk/2011/02/polyholes.html
        
        Args:
            CenterX: X coordinate for hole center
            CenterY: Y coordinate for hole center
            Diameter: Diameter of hole
            IsReference: true if line is a reference line
        """
        ...

    def AddPolyline(self, Line: Polyline, IsReference: bool = False) -> Any:
        """Adds a polyline to the sketch
        
        Args:
            Line: Polyine to add
            IsReference: true if line is a reference line
        """
        ...

    def AddRectangle(self, BottomLeftX: float, BottomLeftY: float, TopRightX: float, TopRightY: float, IsReference: bool = False) -> Any:
        """Adds a rectangle to the sketch
        
        Args:
            BottomLeftX: X coordinate of bottom left corner
            BottomLeftY: Y coordinate of bottom left corner
            TopRightX: X coordinate of top right
            TopRightY: Y coordinate of top right
            IsReference: True to create a reference (default: False) rectangle
        """
        ...

    @overload
    def CopyFrom(self, Source: Sketch) -> Any:
        """Copies a sketch into this sketch
        
        Args:
            Source: Sketch to copy from
        """
        ...

    @overload
    def CopyFrom(self, Source: Sketch, Angle: float, RotationCenterX: float, RotationCenterY: float, TranslateX: float, TranslateY: float, ScaleOriginX: float, ScaleOriginY: float, ScaleFactor: float) -> Any:
        """Copies a sketch into this sketch
        
        Args:
            Source: Sketch to copy from
            Angle: Rotation angle
            RotationCenterX: X-coodinate for center of rotation
            RotationCenterY: Y-coordinate for center of rotation
            TranslateX: Amount to move sketch in X direction
            TranslateY: Amount to move sketch in Y direction
            ScaleOriginX: X-coordinate for scaling origin
            ScaleOriginY: Y-coordinate for scaling origin
            ScaleFactor: Factor for scaling as a percentage
        """
        ...

    @overload
    def ExportSVG(self, FileName: str) -> Any:
        """Exports the sketch to an SVG
        
        Args:
            FileName: Path and name of SVG file to export to
        """
        ...

    @overload
    def ExportSVG(self, FileName: str, IncludeReferences: bool) -> Any:
        """Exports the sketch to an SVG
        
        Args:
            FileName: Path and name of SVG file to export to
            IncludeReferences: true to include reference figures in export
        """
        ...

    @overload
    def ExportSVG(self, FileName: str, IncludeReferences: bool, StrokeWidth: float, StrokeColor: str, StrokeLineCap: str, StrokeDashed: bool, StrokeDashLength: float, ReferenceStrokeWidth: float, ReferenceStrokeColor: str, ReferenceStrokeLineCap: str, ReferenceStrokeDashed: bool, ReferenceStrokeDashLength: float) -> Any:
        """Exports the sketch to an SVG with specific styling
        
        Args:
            FileName: Path and name of SVG file to export to
            IncludeReferences: true to include reference figures in export
            StrokeWidth: Stroke width
            StrokeColor: String containing name of stroke color
            StrokeLineCap: String containing name of stroke line cap type
            StrokeDashed: true if stroke dashed, false if solid
            StrokeDashLength: Length of stroke dashes if dashed
            ReferenceStrokeWidth: Reference stroke width
            ReferenceStrokeColor: String containing name of reference stroke color
            ReferenceStrokeLineCap: String containing name of reference stroke line cap type, can be: butt, round, square
            ReferenceStrokeDashed: true if reference stroke dashed, false if solid
            ReferenceStrokeDashLength: Length of reference stroke dashes if dashed
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
            Part that defines the sketch
        """
        ...

    def GetSelectionAssembly(self) -> Assembly:
        """The assembly that the sketch was selected on
            Only valid when a selection has been made
        
        Returns:
            Assembly or null for no assembly
        """
        ...

    def GetSurface(self) -> Any:
        """Gets the surface that the sketch was created on, e.g.
            a design plane or a face
        
        Returns:
            Plane or Face object
        """
        ...

    def GlobaltoPoint(self, x: float, y: float, z: float) -> Any:
        """Projects a 3D point in the part coordinate system into a point on the sketch
        
        Args:
            x: X coordinate of 3D point
            y: Y coordinate of 3D point
            z: Z coordinate of 3D point
        
        Returns:
            Python list [x, y]
        """
        ...

    @overload
    def ImportSVG(self, FileName: str) -> Any:
        """Imports an SVG into the sketch
        
        Args:
            FileName: Path and name of SVG file
        """
        ...

    @overload
    def ImportSVG(self, FileName: str, TranslateX: float, TranslateY: float, RotationAngle: float, TranslateThenRotate: bool, NativeFigures: bool) -> Any:
        """Imports an SVG into the sketch
        
        Args:
            FileName: Path and name of SVG file
            TranslateX: Amount to translate in the X direction
            TranslateY: Amount to translate in the Y direction
            RotationAngle: Amount to rotate in degrees
            TranslateThenRotate: true to perform translation passed to this function before rotation passed to this function, false to reverse order
            NativeFigures: true to create native circles and arcs when possible, false to always use Bezier curves
        """
        ...

    def LoadXml(self, FileName: str) -> None:
        """Loads the sketch from an XML file
        
        Args:
            FileName: Path and name of file to load from
        """
        ...

    def PointtoGlobal(self, x: float, y: float) -> Any:
        """Converts a point on the sketch into a 3D point in the part coordinate system
        
        Args:
            x: X coordinate of point on sketch
            y: Y coordinate of point on sketch
        
        Returns:
            Python list [x, y, z]
        """
        ...

    def SavetoXml(self, FileName: str) -> None:
        """Saves the sketch to an XML file
            Does not support ellipses and elliptical arcs
        
        Args:
            FileName: Path and name of file to save to
        """
        ...

    @overload
    def StartFaceMapping(self, EdgeVertex1: Vertex, EdgeVertex2: Vertex) -> None:
        """Starts mapping the face so that the specified edge is at [0, 0]
        
        Args:
            EdgeVertex1: Firrt vertex of edge
            EdgeVertex2: Second vertex of edge
        """
        ...

    @overload
    def StartFaceMapping(self, EdgeEndPoint1: List, EdgeEndPoint2: List) -> None:
        """Starts mapping the face so that the specified edge is at [0, 0]
            Affects only the operation of the AddXXX functions and the
            GlobaltoPoint and PointtoGlobal functions, which will now use mapped X and Y values
        
        Args:
            EdgeEndPoint1: First end point of edge [X, Y, Z]
            EdgeEndPoint2: Second end point of edge [X, Y, Z]
        """
        ...

    def StartMapping(self, Point1: List, Point2: List, PointAboveAxis: List) -> None:
        """Starts mapping the sketch so that the specified line is at [0, 0]
            Affects only the operation of the AddXXX functions and the
            GlobaltoPoint and PointtoGlobal functions, which will now use mapped X and Y values
        
        Args:
            Point1: First line end point [X, Y, Z]
            Point2: Second line end point [X, Y, Z]
            PointAboveAxis: Point to be located above the X-axis
        """
        ...

    def StopFaceMapping(self) -> Any:
        """Stops mapping the face
        """
        ...

    def StopMapping(self) -> Any:
        """Stops mapping the sketch
        """
        ...

    def ToXml(self) -> str:
        """Saves the sketch to an XML string
            Does not support ellipses and elliptical arcs
        
        Returns:
            XML string representing sketch
        """
        ...

    # Enums and Constants
    class Constraints:
        """Supported sketch constraints"""
        pass
