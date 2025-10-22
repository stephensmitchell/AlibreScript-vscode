"""Auto-generated Python 3 stub file for AlibreScript API

This file provides type hints and documentation for the AlibreScript API.
Compatible with Python 3.6+ and modern IDEs with type checking support.
"""

from typing import Any, List
from typing import overload


if TYPE_CHECKING:
    from AlibreScript.Assembly import Assembly
    from AlibreScript.Configuration import Configuration
    from AlibreScript.Edge import Edge
    from AlibreScript.Face import Face
    from AlibreScript.Point import Point
    from AlibreScript.Vertex import Vertex


class AssembledPart:

    # Properties (read-only attributes set by Alibre at runtime)
    Configurations: Any  # List of configurations defined on the part
    Name: Any  # Name of the assembled part

    @overload
    def AddPoint(self, Name: str, PointOrVertex: IPoint, XOffset: float, YOffset: float, ZOffset: float) -> Point:
        """Adds a point at an offset to a point or a vertex
        
        Args:
            Name: Name of point
            PointOrVertex: Point or vertex
            XOffset: X offse
            YOffset: Y offset
            ZOffset: Z offset
        
        Returns:
            The created point
        """
        ...

    @overload
    def AddPoint(self, Name: str, PointOrVertex1: IPoint, PointOrVertex2: IPoint, Ratio: float) -> Point:
        """Adds a point between two points/vertices
        
        Args:
            Name: Name of point
            PointOrVertex1: First point or vertex
            PointOrVertex2: Second point or vertex
            Ratio: Ratio of distance between points/vertices
        
        Returns:
            The created point
        """
        ...

    @overload
    def AddPoint(self, Name: str, AxisOrEdge1: IAxis, AxisOrEdge2: IAxis) -> Point:
        """Adds a point at the intersection or two axes or edges
        
        Args:
            Name: Name of point
            AxisOrEdge1: First axis or edge
            AxisOrEdge2: Second axis or edge
        
        Returns:
            The created point
        """
        ...

    @overload
    def AddPoint(self, Name: str, PlaneOrFace1: IPlane, PlaneOrFace2: IPlane, PlaneOrFace3: IPlane) -> Point:
        """Adds a point at the intersection of three planes or faces
        
        Args:
            Name: Name of point
            PlaneOrFace1: First plane or face
            PlaneOrFace2: Second plane or face
            PlaneOrFace3: Third plane or face
        
        Returns:
            The created point
        """
        ...

    @overload
    def AddPoint(self, Name: str, AxisOrEdge: IAxis, PlaneOrFace: IPlane) -> Point:
        """Adds a point at the the intersection of a axis or edge and a plane or face
        
        Args:
            Name: Name of point
            AxisOrEdge: Axis or edge
            PlaneOrFace: Plane or face
        
        Returns:
            The created point
        """
        ...

    @overload
    def AddPoint(self, Name: str, SourcePointOrVertex: IPoint, TargetPlaneOrFace: IPlane, XOffset: float, YOffset: float) -> Point:
        """Adds a point by projecting a point or vertex onto a plane or face
        
        Args:
            Name: Name of point
            SourcePointOrVertex: Point or vertex to project
            TargetPlaneOrFace: Plane or face to project onto
            XOffset: X offset to apply to point once projected
            YOffset: Y offset to apply to point once projected
        
        Returns:
            The created point
        """
        ...

    @overload
    def AddPoint(self, Name: str, TargetEdge: Edge, Ratio: float) -> Point:
        """Adds a point on an edge
        
        Args:
            Name: Name of point
            TargetEdge: The edge to create the point on
            Ratio: Ratio along the edge from 0.0 -> 1.0
        
        Returns:
            The created point
        """
        ...

    def AddPointFromCircularEdge(self, Name: str, TargetEdge: Edge) -> Point:
        """Adds a point at the center of a circular edge
        
        Args:
            Name: Name of point
            TargetEdge: The edge to use for creating the point
        
        Returns:
            The created point
        """
        ...

    def AddPointFromToroidalFace(self, Name: str, TargetFace: Face) -> Point:
        """Adds a point at the center of a toroidal face
        
        Args:
            Name: Name of point
            TargetFace: Toroidal face to use in creating the point
        
        Returns:
            The created point
        """
        ...

    def AssemblyPointtoPartPoint(self, AssemblyPoint: List) -> List[float]:
        """Converts a point in the assembly coordinate system into a point in the part
            coordinate system
        
        Args:
            AssemblyPoint: Point [X, Y, Z] in the assembly coordinate system
        
        Returns:
            Point [X, Y, Z] in the part coordinate system
        """
        ...

    def GetAssembly(self) -> Assembly:
        """Gets the assembly for the part
        
        Returns:
            Assembly or None if no assembly
        """
        ...

    def GetAssemblyBoundingBox(self) -> List[List[float]]:
        """Gets the bounding box for the part as eight points in the assembly coordinate system
        
        Returns:
            Python list of eight points as [P1, P2, ... P8]. Each point is [X, Y, Z]
        """
        ...

    def GetAssemblyVertices(self) -> List[List[float]]:
        """Gets a python list of the current vertices in the part in the assembly coordinate system
        
        Returns:
            Python list of vertices in assembly coordinates [ [X1, Y1, Z1], ... [Xn, Yn, Zn] ]
        """
        ...

    def GetConfiguration(self, Name: str) -> Configuration:
        """Gets a configuration with a specific name
        
        Args:
            Name: Name of confguration
        
        Returns:
            Configuration object
        """
        ...

    def GetEdge(self, Name: str) -> Edge:
        """Gets an edge using it's name "Edge<n>"
        
        Args:
            Name: Name of edge
        
        Returns:
            Edge if found
        """
        ...

    def GetEdges(self) -> List[Edge]:
        """Gets a python list of the current edges in the part
        
        Returns:
            Python list of edges
        """
        ...

    def GetFace(self, Name: str) -> Face:
        """Gets a face using it's name "Face<n>"
        
        Args:
            Name: Name of face
        
        Returns:
            Face if found
        """
        ...

    def GetFaces(self) -> List[Face]:
        """Gets a python list of the current faces in the part
        
        Returns:
            Python list of faces
        """
        ...

    def GetMappedOccurrence(self, Assembly: IADAssemblySession) -> Any:
        """Gets the occurrence of the part mapped into the 
            occurrence structure of a specific assembly
            This occurrence can be used to create constraints in the specific
            assembly using the part
        
        Args:
            Assembly: Assembly for occurrence structure
        
        Returns:
            Mapped occurrence or null if not found
        """
        ...

    def PartPointtoAssemblyPoint(self, PartPoint: List) -> List[float]:
        """Converts a point in the part coordinate system into a point in the assembly
            coordinate system
        
        Args:
            PartPoint: Point [X, Y, Z] in the part coordinate system
        
        Returns:
            Point [X, Y, Z] in the assembly coordinate system
        """
        ...
