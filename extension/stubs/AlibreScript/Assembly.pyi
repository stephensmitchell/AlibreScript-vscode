"""Auto-generated Python 3 stub file for AlibreScript API

This file provides type hints and documentation for the AlibreScript API.
Compatible with Python 3.6+ and modern IDEs with type checking support.
"""

from __future__ import annotations
from typing import Any, List, TYPE_CHECKING
from typing import overload

if TYPE_CHECKING:
    from AlibreScript.AssembledPart import AssembledPart
    from AlibreScript.AssembledSubAssembly import AssembledSubAssembly
    from AlibreScript.Configuration import Configuration
    from AlibreScript.Parameter import Parameter


class Assembly:

    @overload
    def __init__(self, folder: str, name: str) -> None:
        """Opens an existing assembly

        Args:
            folder: Folder containing assembly
            name: Name of assembly to open
        """
        ...

    @overload
    def __init__(self, folder: str, name: str, hide_editor: bool) -> None:
        """Opens an existing assembly, optionally hiding the editor

        Args:
            folder: Folder containing assembly
            name: Name of assembly to open
            hide_editor: True to hide the editor
        """
        ...

    @overload
    def __init__(self, name: str) -> None:
        """Creates a new assembly

        Args:
            name: Name of new assembly
        """
        ...

    @overload
    def __init__(self, name: str, create_new: bool) -> None:
        """Creates a new assembly or accesses an already opened assembly

        Args:
            name: Name of assembly to create or access
            create_new: True to create a new assembly, false to access an opened assembly
        """
        ...

    @overload
    def __init__(self, name: str, create_new: bool, hide_editor: bool) -> None:
        """Creates a new assembly or accesses an already opened assembly, optionally hiding the editor

        Args:
            name: Name of assembly to create or access
            create_new: True to create a new assembly, false to access an opened assembly
            hide_editor: True to hide the editor (only valid if assembly is not already open)
        """
        ...

    # Properties (read-only attributes set by Alibre at runtime)
    Comment: Any  # Comment property
    Configurations: Any  # A list of configurations defined on the assembly
    CostCenter: Any  # Cost center property
    CreatedBy: Any  # Created By property
    CreatedDate: Any  # Created Date property
    CreatingApplication: Any  # Creating Application property
    Density: Any  # Density of the part
    Description: Any  # Description of the part
    DocumentNumber: Any  # Document Number property
    EngineeringApprovalDate: Any  # Engineering Approval Date property
    EngineeringApprovedBy: Any  # Engineering Approved By property
    EstimatedCost: Any  # Estimated Cost property
    ExtendedMaterialInformation: Any  # Material (extended information) property
    FileName: Any  # Path and filename of the assembly
    Keywords: Any  # Keywords property
    LastAuthor: Any  # Last Author property
    LastUpdateDate: Any  # Last Update Date property
    ManufacturingApprovedBy: Any  # Manufacturing Approved By property
    ManufacturingApprovedDate: Any  # Product property
    Material: Any  # Material of the part
    ModifiedInformation: Any  # Modified Information property
    Name: Any  # Name of the assembly
    Number: Any  # User-defined number for the part
    Origin: Any  # Gets the origin (language independent)
    Parameters: Any  # A list of parameters defined on the assembly
    Parts: Any  # A list of parts defined on the assembly
    Product: Any  # Product property
    ReceivedFrom: Any  # Received From property
    Revision: Any  # Revision property
    Selections: Any  # Gets the currently selected items as [ItemA, ItemB, ...]             Supports subassemblies, parts, faces, edges, vertices, planes, axes and points
    StockSize: Any  # Stock Size property
    SubAssemblies: Any  # A list of subassemblies defined on the assembly
    Supplier: Any  # Supplier property
    Title: Any  # Title property
    Vendor: Any  # Vendor property
    WebLink: Any  # Web Link property
    XAxis: Any  # Gets the X-axis (language independent)
    XYPlane: Any  # Gets the XY-plane (language independent)
    YAxis: Any  # Gets the Y-axis (language independent)
    YZPlane: Any  # Gets the YZ-plane (language independent)
    ZAxis: Any  # Gets the Z-axis (language independent)
    ZXPlane: Any  # Gets the ZX-plane (language independent)

    @overload
    def AddAlignConstraint(self, Distance: float, PartorAssemblyA: IAssembled, ItemA: IConstrainable, PartorAssemblyB: IAssembled, ItemB: IConstrainable) -> Any:
        """Adds a simple alignment constraint between two planes/faces/axes/edges/points
        
        Args:
            Distance: Alignment distance
            PartorAssemblyA: First part/assembly to constrain
            ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
            PartorAssemblyB: Second part/assembly to constrain
            ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
        """
        ...

    @overload
    def AddAlignConstraint(self, Distance: float, PartorAssemblyA: IAssembled, ItemA: IConstrainable, PartorAssemblyB: IAssembled, ItemB: IConstrainable, IsReversed: bool, Name: str) -> Any:
        """Adds a simple alignment constraint between two planes/faces/axes/edges/points
        
        Args:
            Distance: Alignment distance
            PartorAssemblyA: First part/assembly to constrain
            ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
            PartorAssemblyB: Second part/assembly to constrain
            ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
            IsReversed: true to reverse constraint
            Name: Name of constraint
        """
        ...

    def AddAlignConstraint2(self, Distance1: float, Distance2: float, PartorAssemblyA: IAssembled, ItemA: IConstrainable, PartorAssemblyB: IAssembled, ItemB: IConstrainable, IsReversed: bool, Name: str, BoundsType: ConstraintBoundsType) -> Any:
        """Adds an alignment constraint between two planes/faces/axes/edges/points
            Uses bounds type
        
        Args:
            Distance1: Align distance
            Distance2: Second distance for 'between' bounds type or zero if not used
            PartorAssemblyA: First part/assembly to constrain
            ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
            PartorAssemblyB: Second part/assembly to constrain
            ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
            IsReversed: true to reverse constraint
            Name: Name of constraint
            BoundsType: The bounds type to use
        """
        ...

    @overload
    def AddAngleConstraint(self, Angle: float, PartorAssemblyA: IAssembled, ItemA: IConstrainable, PartorAssemblyB: IAssembled, ItemB: IConstrainable) -> Any:
        """Adds an angle constraint between two planes/faces/axes/edges/points
        
        Args:
            Angle: Angle in degrees
            PartorAssemblyA: First part/assembly to constrain
            ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
            PartorAssemblyB: Second part/assembly to constrain
            ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
        """
        ...

    @overload
    def AddAngleConstraint(self, Angle: float, PartorAssemblyA: IAssembled, ItemA: IConstrainable, PartorAssemblyB: IAssembled, ItemB: IConstrainable, IsReversed: bool, Name: str) -> Any:
        """Adds a simple angle constraint between two planes/faces/axes/edges/points
        
        Args:
            Angle: Angle in degrees
            PartorAssemblyA: First part/assembly to constrain
            ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
            PartorAssemblyB: Second part/assembly to constrain
            ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
            IsReversed: true to reverse constraint
            Name: Name of constraint
        """
        ...

    def AddAngleConstraint2(self, Angle1: float, Angle2: float, PartorAssemblyA: IAssembled, ItemA: IConstrainable, PartorAssemblyB: IAssembled, ItemB: IConstrainable, IsReversed: bool, Name: str, BoundsType: ConstraintBoundsType) -> Any:
        """Adds an angle constraint between two planes/faces/axes/edges/points
            Uses bounds type
        
        Args:
            Angle1: Angle for constraint
            Angle2: Second angle for 'between' bounds type or zero if not used
            PartorAssemblyA: First part/assembly to constrain
            ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
            PartorAssemblyB: Second part/assembly to constrain
            ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
            IsReversed: true to reverse constraint
            Name: Name of constraint
            BoundsType: The bounds type to use
        """
        ...

    @overload
    def AddAxis(self, Name: str, Plane1: ISketchSurface, Plane2: ISketchSurface) -> Axis:
        """Creates an axis based on the intersection of two planes/faces
        
        Args:
            Name: Name of axis
            Plane1: First plane/face
            Plane2: Second plane/face
        
        Returns:
            New Axis
        """
        ...

    @overload
    def AddAxis(self, Name: str, Point1: List, Point2: List) -> Axis:
        """Creates an axis based on two points
        
        Args:
            Name: Name of axis
            Point1: First point
            Point2: Second point
        
        Returns:
            New axis
        """
        ...

    @overload
    def AddConfiguration(self, Name: str) -> Configuration:
        """Adds a configuration to the assembly
        
        Args:
            Name: Name of configuration
        
        Returns:
            New configuration
        """
        ...

    @overload
    def AddConfiguration(self, Name: str, BaseConfigurationName: str) -> Configuration:
        """Adds a configuration to the assembly using another configuration as a base
        
        Args:
            Name: Name of configuration
            BaseConfigurationName: Name of base configuration to use
        
        Returns:
            New configuration
        """
        ...

    def AddFastenerConstraint(self, Distance: float, PartorAssemblyA: IAssembled, ItemA: IConstrainable, PartorAssemblyB: IAssembled, ItemB: IConstrainable, IsReversed: bool, Name: str) -> Any:
        """Adds a fastner constraint
        
        Args:
            Distance: Fastener to surface mate distance
            PartorAssemblyA: First part/assembly to constrain
            ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
            PartorAssemblyB: Second part/assembly to constrain
            ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
            IsReversed: true to reverse constraint
            Name: Name of constraint
        """
        ...

    def AddFastenerConstraint2(self, Distance1: float, Distance2: float, PartorAssemblyA: IAssembled, ItemA: IConstrainable, PartorAssemblyB: IAssembled, ItemB: IConstrainable, IsReversed: bool, Name: str, BoundsType: ConstraintBoundsType) -> Any:
        """Adds a fastner constraint
        
        Args:
            Distance1: Fastener to surface mate distance
            Distance2: Second distance for 'between' bounds type or zero if not used
            PartorAssemblyA: First part/assembly to constrain
            ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
            PartorAssemblyB: Second part/assembly to constrain
            ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
            IsReversed: true to reverse constraint
            Name: Name of constraint
            BoundsType: The bounds type to use
        """
        ...

    def AddGearConstraint(self, RatioA: float, RatioB: float, PartorAssemblyA: IAssembled, ItemA: IConstrainable, PartorAssemblyB: IAssembled, ItemB: IConstrainable, IsReversed: bool, Name: str) -> Any:
        """Adds a gear constraint using ratio RatioA:RatioB
        
        Args:
            RatioA: First value in gear ratio
            RatioB: Second value in gear ratio
            PartorAssemblyA: First part/assembly to constrain
            ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
            PartorAssemblyB: Second part/assembly to constrain
            ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
            IsReversed: true to reverse constraint
            Name: Name of constraint
        """
        ...

    @overload
    def AddMateConstraint(self, Distance: float, PartorAssemblyA: IAssembled, ItemA: IConstrainable, PartorAssemblyB: IAssembled, ItemB: IConstrainable) -> Any:
        """Adds a simple mate constraint between two planes/faces/axes/edges/points
        
        Args:
            Distance: Mate distance
            PartorAssemblyA: First part/assembly to constrain
            ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
            PartorAssemblyB: Second part/assembly to constrain
            ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
        """
        ...

    @overload
    def AddMateConstraint(self, Distance: float, PartorAssemblyA: IAssembled, ItemA: IConstrainable, PartorAssemblyB: IAssembled, ItemB: IConstrainable, IsReversed: bool, Name: str) -> Any:
        """Adds a simple mate constraint between two planes/faces/axes/edges/points
        
        Args:
            Distance: Mate distance
            PartorAssemblyA: First part/assembly to constrain
            ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
            PartorAssemblyB: Second part/assembly to constrain
            ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
            IsReversed: true to reverse constraint
            Name: Name of constraint
        """
        ...

    def AddMateConstraint2(self, Distance1: float, Distance2: float, PartorAssemblyA: IAssembled, ItemA: IConstrainable, PartorAssemblyB: IAssembled, ItemB: IConstrainable, IsReversed: bool, Name: str, BoundsType: ConstraintBoundsType) -> Any:
        """Adds a mate constraint between two planes/faces/axes/edges/points
            Uses bounds type
        
        Args:
            Distance1: Mate distance
            Distance2: Second distance for 'between' bounds type or zero if not used
            PartorAssemblyA: First part/assembly to constrain
            ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
            PartorAssemblyB: Second part/assembly to constrain
            ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
            IsReversed: true to reverse constraint
            Name: Name of constraint
            BoundsType: The bounds type to use
        """
        ...

    def AddNewPart(self, Name: str, X: float, Y: float, Z: float) -> Part:
        """Adds a new part to the assembly
        
        Args:
            Name: Name of the new part
            X: X location of part
            Y: Y location of part
            Z: Z location of part
        
        Returns:
            New part
        """
        ...

    def AddNewSubAssembly(self, Name: str, X: float, Y: float, Z: float) -> Assembly:
        """Adds a new sub-assembly to the assembly
        
        Args:
            Name: Name of the new assembly
            X: X location of assembly
            Y: Y location of assembly
            Z: Z location of assembly
        
        Returns:
            New part
        """
        ...

    @overload
    def AddOrientConstraint(self, Value: float, PartorAssemblyA: IAssembled, ItemA: IConstrainable, PartorAssemblyB: IAssembled, ItemB: IConstrainable) -> Any:
        """Adds an orient constraint between two planes/faces/axes/edges/points
        
        Args:
            Value: Value
            PartorAssemblyA: First part/assembly to constrain
            ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
            PartorAssemblyB: Second part/assembly to constrain
            ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
        """
        ...

    @overload
    def AddOrientConstraint(self, Value: float, PartorAssemblyA: IAssembled, ItemA: IConstrainable, PartorAssemblyB: IAssembled, ItemB: IConstrainable, IsReversed: bool, Name: str) -> Any:
        """Adds an orient constraint between two planes/faces/axes/edges/points
        
        Args:
            Value: Value
            PartorAssemblyA: First part/assembly to constrain
            ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
            PartorAssemblyB: Second part/assembly to constrain
            ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
            IsReversed: true to reverse constraint
            Name: Name of constraint
        """
        ...

    @overload
    def AddParameter(self, Name: str, Type: ParameterTypes, Value: float) -> Parameter:
        """Adds a parameter to the assembly
        
        Args:
            Name: Name of parameter
            Type: Type of parameter
            Value: Value for parameter
        
        Returns:
            New parameter
        """
        ...

    @overload
    def AddParameter(self, Name: str, Type: ParameterTypes, Equation: str) -> Parameter:
        """Adds a parameter to the assembly
            NOTE: DOESN'T SEEM TO WORK IN GD V16 - THROWS EXCEPTION ABOUT TRANSACTION ALREADY BEING OPEN
        
        Args:
            Name: Name of parameter
            Type: Type of parameter
            Equation: Equation for parameter
        
        Returns:
            New parameter
        """
        ...

    @overload
    def AddPart(self, Folder: str, Name: str) -> Any:
        """Adds a part to the assembly at the origin
        
        Args:
            Folder: Folder containing part
            Name: Name of part to open
        
        Returns:
            The added part
        """
        ...

    @overload
    def AddPart(self, Folder: str, Name: str, OffsetX: float, OffsetY: float, OffsetZ: float) -> Any:
        """Adds a part to the assembly
        
        Args:
            Folder: Folder containing part
            Name: Name of part to open
            OffsetX: X offset
            OffsetY: Y offset
            OffsetZ: Z offset
        
        Returns:
            The added part
        """
        ...

    @overload
    def AddPart(self, Folder: str, Name: str, OffsetX: float, OffsetY: float, OffsetZ: float, AngleX: float, AngleY: float, AngleZ: float, TranslationFirst: bool) -> Any:
        """Adds a part to the assembly
        
        Args:
            Folder: Folder containing part
            Name: Name of part to open
            OffsetX: X offset
            OffsetY: Y offset
            OffsetZ: Z offset
            AngleX: X rotation angle in degrees
            AngleY: Y rotation angle in degrees
            AngleZ: Z rotation angle in degrees
            TranslationFirst: if true translation occurs before rotation, if false rotation
            occurs before translation
        
        Returns:
            The added part
        """
        ...

    @overload
    def AddPart(self, Part: Part) -> Any:
        """Adds a part to the assembly at the origin
        
        Args:
            Part: Part to add
        
        Returns:
            The added part
        """
        ...

    @overload
    def AddPart(self, Part: Part, OffsetX: float, OffsetY: float, OffsetZ: float) -> Any:
        """Adds a part to the assembly
        
        Args:
            Part: Part to add
            OffsetX: X offset
            OffsetY: Y offset
            OffsetZ: Z offset
        
        Returns:
            The added part
        """
        ...

    @overload
    def AddPart(self, FileName: str) -> Any:
        """Adds a part to the assembly at the origin
        
        Args:
            FileName: Path and name of part to open
        
        Returns:
            The added part
        """
        ...

    @overload
    def AddPart(self, FileName: str, OffsetX: float, OffsetY: float, OffsetZ: float) -> Any:
        """Adds a part to the assembly
        
        Args:
            FileName: Path and name of part to open
            OffsetX: X offset
            OffsetY: Y offset
            OffsetZ: Z offset
        
        Returns:
            The added part
        """
        ...

    @overload
    def AddPart(self, FileName: str, OffsetX: float, OffsetY: float, OffsetZ: float, AngleX: float, AngleY: float, AngleZ: float, TranslationFirst: bool) -> Any:
        """Adds a part to the assembly
        
        Args:
            FileName: Path and name of part to open
            OffsetX: X offset
            OffsetY: Y offset
            OffsetZ: Z offset
            AngleX: X rotation angle in degrees
            AngleY: Y rotation angle in degrees
            AngleZ: Z rotation angle in degrees
            TranslationFirst: if true translation occurs before rotation, if false rotation
            occurs before translation
        
        Returns:
            The added part
        """
        ...

    @overload
    def AddPart(self, Part: Part, OffsetX: float, OffsetY: float, OffsetZ: float, AngleX: float, AngleY: float, AngleZ: float, TranslationFirst: bool) -> Any:
        """Adds a part to the assembly
        
        Args:
            Part: Part to add
            OffsetX: X offset
            OffsetY: Y offset
            OffsetZ: Z offset
            AngleX: X rotation angle in degrees
            AngleY: Y rotation angle in degrees
            AngleZ: Z rotation angle in degrees
            TranslationFirst: if true translation occurs before rotation, if false rotation
            occurs before translation
        
        Returns:
            The added part
        """
        ...

    @overload
    def AddPlane(self, Name: str, SourcePlane: ISketchSurface, Offset: float) -> Plane:
        """Creates a plane based on the offset from an existing plane
        
        Args:
            Name: Name of plane
            SourcePlane: Plane/face to use as basis
            Offset: Offset from basis plane in currently chosen units
        
        Returns:
            Created plane
        """
        ...

    @overload
    def AddPlane(self, Name: str, NormalVector: List, PointonPlane: List) -> Plane:
        """Adds a plane using a normal vector and a point on the plane
        
        Args:
            Name: Name of plane to add
            NormalVector: Normal vector as a list [nx, ny, nz]. Does not need to be a unit vector
            PointonPlane: A point on the plane as a list [px, py, pz]
        
        Returns:
            Created plane
        """
        ...

    @overload
    def AddPlane(self, Name: str, SourcePlane: ISketchSurface, RotationAxis: Axis, Angle: float) -> Plane:
        """Creates a new plane at an angle to an existing plane
        
        Args:
            Name: Name of new plane
            SourcePlane: Plane/face to use as basis for new plane
            RotationAxis: Axis of rotation for new plane
            Angle: Angle of new plane in degrees
        
        Returns:
            New plane
        """
        ...

    @overload
    def AddPlane(self, Name: str, Point1: List, Point2: List, Point3: List) -> Plane:
        """Creates a plane using three points
        
        Args:
            Name: Name of plane
            Point1: Point on plane
            Point2: Point on plane
            Point3: Point on plane
        
        Returns:
            Created plane
        """
        ...

    @overload
    def AddPoint(self, Name: str, PointOrVertex: IPoint, XOffset: float, YOffset: float, ZOffset: float) -> Point:
        """Add a point at an offset to a point or a vertex
        
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
        """Add a point between two points/vertices
        
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
        """Add a point at the intersection or two axes or edges
        
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
        """Add a point at the intersection of three planes or faces
        
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
        """Add a point at the the intersection of a axis or edge and a plane or face
        
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
        """Add a point by projecting a point or vertex onto a plane or face
        
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
        """Add a point on an edge
        
        Args:
            Name: Name of point
            TargetEdge: The edge to create the point on
            Ratio: Ratio along the edge from 0.0 -> 1.0
        
        Returns:
            The created point
        """
        ...

    @overload
    def AddPoint(self, Name: str, X: float, Y: float, Z: float) -> Point:
        """Adds a point to the assembly
        
        Args:
            Name: Name of new point
            X: X coordinate
            Y: Y coordinate
            Z: Z coordinate
        
        Returns:
            The new point
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

    def AddPoints(self, Prefix: str, Points: List) -> Point:
        """Adds a set of points to the part
        
        Args:
            Prefix: Prefix for the point names
            Points: List of points [x1,y1,z1, ..., xn,yn,zn]
        """
        ...

    def AddRackAndPinionConstraint(self, PitchDiameter: float, PartorAssemblyA: IAssembled, ItemA: IConstrainable, PartorAssemblyB: IAssembled, ItemB: IConstrainable, IsReversed: bool, Name: str) -> Any:
        """Adds a rack and pinion constraint
        
        Args:
            PitchDiameter: Pitch diameter
            PartorAssemblyA: First part/assembly to constrain
            ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
            PartorAssemblyB: Second part/assembly to constrain
            ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
            IsReversed: true to reverse constraint
            Name: Name of constraint
        """
        ...

    def AddScrewConstraint(self, ThreadPitch: float, PartorAssemblyA: IAssembled, ItemA: IConstrainable, PartorAssemblyB: IAssembled, ItemB: IConstrainable, IsReversed: bool, Name: str) -> Any:
        """Adds a screw constraint
        
        Args:
            ThreadPitch: Pitch of thread
            PartorAssemblyA: First part/assembly to constrain
            ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
            PartorAssemblyB: Second part/assembly to constrain
            ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
            IsReversed: true to reverse constraint
            Name: Name of constraint
        """
        ...

    @overload
    def AddSubAssembly(self, FileName: str, OffsetX: float, OffsetY: float, OffsetZ: float) -> Any:
        """Adds a sub-assembly to the assembly
        
        Args:
            FileName: Path and name of sub-assembly to open
            OffsetX: X offset
            OffsetY: Y offset
            OffsetZ: Z offset
        
        Returns:
            The added sub-assembly
        """
        ...

    @overload
    def AddSubAssembly(self, FileName: str, OffsetX: float, OffsetY: float, OffsetZ: float, AngleX: float, AngleY: float, AngleZ: float, TranslationFirst: bool) -> Any:
        """Adds a sub-assembly to the assembly
        
        Args:
            FileName: Path and name of sub-asembly to open
            OffsetX: X offset
            OffsetY: Y offset
            OffsetZ: Z offset
            AngleX: X rotation angle in degrees
            AngleY: Y rotation angle in degrees
            AngleZ: Z rotation angle in degrees
            TranslationFirst: if true translation occurs before rotation, if false rotation
            occurs before translation
        
        Returns:
            The added assembly
        """
        ...

    @overload
    def AddSubAssembly(self, Assembly: Assembly) -> Any:
        """Adds a sub-assembly to the assembly at the origin
        
        Args:
            Assembly: Assembly to add
        
        Returns:
            The added assembly
        """
        ...

    @overload
    def AddSubAssembly(self, Assembly: Assembly, OffsetX: float, OffsetY: float, OffsetZ: float) -> Any:
        """Adds a sub-assembly to the assembly
        
        Args:
            Assembly: Assembly to add
            OffsetX: X offset
            OffsetY: Y offset
            OffsetZ: Z offset
        
        Returns:
            The added assembly
        """
        ...

    @overload
    def AddSubAssembly(self, Assembly: Assembly, OffsetX: float, OffsetY: float, OffsetZ: float, AngleX: float, AngleY: float, AngleZ: float, TranslationFirst: bool) -> Any:
        """Adds a sub-assembly to the assembly
        
        Args:
            Assembly: Sub-assembly to add
            OffsetX: X offset
            OffsetY: Y offset
            OffsetZ: Z offset
            AngleX: X rotation angle in degrees
            AngleY: Y rotation angle in degrees
            AngleZ: Z rotation angle in degrees
            TranslationFirst: if true translation occurs before rotation, if false rotation
            occurs before translation
        
        Returns:
            The added sub-assembly
        """
        ...

    @overload
    def AddSubAssembly(self, Folder: str, Name: str) -> Any:
        """Adds a sub-assembly to the assembly at the origin
        
        Args:
            Folder: Folder containing sub-assembly
            Name: Name of sub-assembly to open
        
        Returns:
            The added sub-assembly
        """
        ...

    @overload
    def AddSubAssembly(self, Folder: str, Name: str, OffsetX: float, OffsetY: float, OffsetZ: float) -> Any:
        """Adds a sub-assembly to the assembly
        
        Args:
            Folder: Folder containing sub-assembly
            Name: Name of sub-assembly to open
            OffsetX: X offset
            OffsetY: Y offset
            OffsetZ: Z offset
        
        Returns:
            The added sub-assembly
        """
        ...

    @overload
    def AddSubAssembly(self, Folder: str, Name: str, OffsetX: float, OffsetY: float, OffsetZ: float, AngleX: float, AngleY: float, AngleZ: float, TranslationFirst: bool) -> Any:
        """Adds a sub-assembly to the assembly
        
        Args:
            Folder: Folder containing sub-assembly
            Name: Name of sub-assembly to open
            OffsetX: X offset
            OffsetY: Y offset
            OffsetZ: Z offset
            AngleX: X rotation angle in degrees
            AngleY: Y rotation angle in degrees
            AngleZ: Z rotation angle in degrees
            TranslationFirst: if true translation occurs before rotation, if false rotation
            occurs before translation
        
        Returns:
            The added sub-assembly
        """
        ...

    @overload
    def AddSubAssembly(self, FileName: str) -> Any:
        """Adds a sub-assembly to the assembly at the origin
        
        Args:
            FileName: Path and name of sub-assembly to open
        
        Returns:
            The added sub-assembly
        """
        ...

    @overload
    def AddTangentConstraint(self, Distance: float, PartorAssemblyA: IAssembled, ItemA: IConstrainable, PartorAssemblyB: IAssembled, ItemB: IConstrainable, Outside: bool) -> Any:
        """Adds a tangent constraint between two planes/faces/axes/edges/points
        
        Args:
            Distance: Alignment distance
            PartorAssemblyA: First part/assembly to constrain
            ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
            PartorAssemblyB: Second part/assembly to constrain
            ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
            Outside: true for an outside tangent constraint, false for an inside tangent constraint
        """
        ...

    @overload
    def AddTangentConstraint(self, Distance: float, PartorAssemblyA: IAssembled, ItemA: IConstrainable, PartorAssemblyB: IAssembled, ItemB: IConstrainable, Outside: bool, IsReversed: bool, Name: str) -> Any:
        """Adds a tangent constraint between two planes/faces/axes/edges/points
        
        Args:
            Distance: Alignment distance
            PartorAssemblyA: First part/assembly to constrain
            ItemA: Plane/face/axis/edge/point on first part/assembly to constrain
            PartorAssemblyB: Second part/assembly to constrain
            ItemB: Plane/face/axis/edge/point on second part/assembly to constrain
            Outside: true for an outside tangent constraint, false for an inside tangent constraint
            IsReversed: true to reverse constraint
            Name: Name of constraint
        """
        ...

    @overload
    def AnchorPart(self, Name: str) -> Any:
        """Anchors a part
        
        Args:
            Name: Name of part to anchor
        """
        ...

    @overload
    def AnchorPart(self, Part: AssembledPart) -> Any:
        """Anchors a part
        
        Args:
            Part: Part to anchor
        """
        ...

    def AnchorSubAssembly(self, Name: str) -> Any:
        """Anchors a sub-assembly
        
        Args:
            Name: Name of sub-assembly to anchor
        """
        ...

    def Close(self) -> None:
        """Closes the assembly
            If it is unsaved then changes will be lost
        """
        ...

    def CreateUniqueName(self, BaseName: str) -> Any:
        """Creates a unique name that can be used to safely add a part or subassembly to the assembly
            if the names used in the assembly are not known in advance
        
        Args:
            BaseName: Base name to use
        
        Returns:
            Unique name
        """
        ...

    def DisplayUnits(self) -> Any:
        """Gets the display units for the assembly
        
        Returns:
            The display units
        """
        ...

    @overload
    def DuplicatePart(self, Name: str, OffsetX: float, OffsetY: float, OffsetZ: float) -> Any:
        """Duplicates a part in the assembly
        
        Args:
            Name: Name of part to duplicate
            OffsetX: X offset
            OffsetY: Y offset
            OffsetZ: Z offset
        
        Returns:
            The duplicate part
        """
        ...

    @overload
    def DuplicatePart(self, Part: AssembledPart, OffsetX: float, OffsetY: float, OffsetZ: float) -> Any:
        """Duplicates a part in the assembly
        
        Args:
            Part: Part to duplicate
            OffsetX: X offset
            OffsetY: Y offset
            OffsetZ: Z offset
        
        Returns:
            The duplicate part
        """
        ...

    @overload
    def DuplicatePart(self, Name: str, OffsetX: float, OffsetY: float, OffsetZ: float, AngleX: float, AngleY: float, AngleZ: float, TranslationFirst: bool) -> Any:
        """Duplicates a part in the assembly
        
        Args:
            Name: Name of part to duplicate
            OffsetX: X offset
            OffsetY: Y offset
            OffsetZ: Z offset
            AngleX: X rotation angle in degrees
            AngleY: Y rotation angle in degrees
            AngleZ: Z rotation angle in degrees
            TranslationFirst: if true translation occurs before rotation, if false rotation
            occurs before translation
        
        Returns:
            The duplicate part
        """
        ...

    @overload
    def DuplicatePart(self, Part: AssembledPart, OffsetX: float, OffsetY: float, OffsetZ: float, AngleX: float, AngleY: float, AngleZ: float, TranslationFirst: bool) -> Any:
        """Duplicates a part in the assembly
        
        Args:
            Part: Part to duplicate
            OffsetX: X offset
            OffsetY: Y offset
            OffsetZ: Z offset
            AngleX: X rotation angle in degrees
            AngleY: Y rotation angle in degrees
            AngleZ: Z rotation angle in degrees
            TranslationFirst: if true translation occurs before rotation, if false rotation
            occurs before translation
        
        Returns:
            The duplicate part
        """
        ...

    @overload
    def DuplicateSubAssembly(self, SubAssembly: AssembledSubAssembly, OffsetX: float, OffsetY: float, OffsetZ: float) -> Any:
        """Duplicates a sub-assembly in the assembly
        
        Args:
            SubAssembly: Sub-assembly to duplicate
            OffsetX: X offset
            OffsetY: Y offset
            OffsetZ: Z offset
        
        Returns:
            The duplicate sub-assembly
        """
        ...

    @overload
    def DuplicateSubAssembly(self, Name: str, OffsetX: float, OffsetY: float, OffsetZ: float) -> Any:
        """Duplicates a sub-assembly in the assembly
        
        Args:
            Name: Name of sub-assembly to duplicate
            OffsetX: X offset
            OffsetY: Y offset
            OffsetZ: Z offset
        
        Returns:
            The duplicate sub-assembly
        """
        ...

    @overload
    def DuplicateSubAssembly(self, SubAssembly: AssembledSubAssembly, OffsetX: float, OffsetY: float, OffsetZ: float, AngleX: float, AngleY: float, AngleZ: float, TranslationFirst: bool) -> Any:
        """Duplicates a sub-assembly in the assembly
        
        Args:
            SubAssembly: Sub-assembly to duplicate
            OffsetX: X offset
            OffsetY: Y offset
            OffsetZ: Z offset
            AngleX: X rotation angle in degrees
            AngleY: Y rotation angle in degrees
            AngleZ: Z rotation angle in degrees
            TranslationFirst: if true translation occurs before rotation, if false rotation
            occurs before translation
        
        Returns:
            The duplicate sub-assembly
        """
        ...

    @overload
    def DuplicateSubAssembly(self, Name: str, OffsetX: float, OffsetY: float, OffsetZ: float, AngleX: float, AngleY: float, AngleZ: float, TranslationFirst: bool) -> Any:
        """Duplicates a sub-assembly in the assembly
        
        Args:
            Name: Name of sub-assembly to duplicate
            OffsetX: X offset
            OffsetY: Y offset
            OffsetZ: Z offset
            AngleX: X rotation angle in degrees
            AngleY: Y rotation angle in degrees
            AngleZ: Z rotation angle in degrees
            TranslationFirst: if true translation occurs before rotation, if false rotation
            occurs before translation
        
        Returns:
            The duplicate sub-assembly
        """
        ...

    def ExportBIP(self, FileName: str) -> Any:
        """Exports a keyshot file
        
        Args:
            FileName: Path and name of keyshot file
        """
        ...

    def ExportIGES(self, FileName: str) -> Any:
        """Exports the assembly as a IGES file
        
        Args:
            FileName: Path and name of IGES file
        """
        ...

    def ExportSAT(self, FileName: str, Version: int, SaveColors: bool) -> Any:
        """Exports the assembly as a SAT file
        
        Args:
            FileName: Path and name of SAT file
            Version: Exported SAT file version
            SaveColors: true to preseve colors
        """
        ...

    def ExportSTEP203(self, FileName: str) -> Any:
        """Exports the assembly as a STEP 203 file
        
        Args:
            FileName: Path and name of STEP 203 file
        """
        ...

    def ExportSTEP214(self, FileName: str) -> Any:
        """Exports the assembly as a STEP 214 file
        
        Args:
            FileName: Path and name of STEP 214 file
        """
        ...

    def ExportSTL(self, FileName: str) -> Any:
        """Exports the assembly as an STL file
        
        Args:
            FileName: Path and name of STL file
        """
        ...

    def GetActiveConfiguration(self) -> Any:
        """Gets the currently active configuration
        
        Returns:
            Configuration object
        """
        ...

    def GetAxis(self, Name: str) -> Axis:
        """Gets an axis from an axis name
        
        Args:
            Name: Name of axis to find
        
        Returns:
            Found axis
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

    def GetCustomProperty(self, Name: str) -> Any:
        """Gets the value of a custonm property
        
        Args:
            Name: Name of the custom property
        
        Returns:
            The value of the property as a string
        """
        ...

    def GetParameter(self, Name: str) -> Parameter:
        """Gets a parameter with a specific name
        
        Args:
            Name: Name of parameter
        
        Returns:
            Parameter object
        """
        ...

    def GetPart(self, Name: str) -> AssembledPart:
        """Gets a part in the assembly
        
        Args:
            Name: Name of part instance to get
        
        Returns:
            The part
        """
        ...

    @overload
    def GetPartOrientation(self, Part: AssembledPart) -> Part:
        """Gets the orientation of a part in an assembly
        
        Args:
            Part: Part in an assembly
        
        Returns:
            Part orientation as [OffsetX, OffsetY, OffsetZ, AngleX, AngleY, AngleZ], translation before rotation
        """
        ...

    @overload
    def GetPartOrientation(self, PartName: str) -> Part:
        """Gets the orientation of a part in an assembly
        
        Args:
            PartName: Name of part to get orientation
        
        Returns:
            Part orientation as [OffsetX, OffsetY, OffsetZ, AngleX, AngleY, AngleZ], translation before rotation
        """
        ...

    def GetPlane(self, Name: str) -> Plane:
        """Gets a plane using the name of the plane
        
        Args:
            Name: Name of plane to find
        
        Returns:
            The plane
        """
        ...

    def GetPoint(self, Name: str) -> Point:
        """Gets a point on the assembly using the point name. The point must have been created in a script
        
        Args:
            Name: Name of point to get
        
        Returns:
            The point
        """
        ...

    def GetSubAssembly(self, Name: str) -> AssembledSubAssembly:
        """Gets a sub-assembly in the assembly
        
        Args:
            Name: Name of sub-assembly instance to get
        
        Returns:
            The sub-assembly
        """
        ...

    def GetUserData(self, Name: str) -> Any:
        """Gets user data
        
        Args:
            Name: Name of data to get
        
        Returns:
            Data as a python dictionary or None if not found
        """
        ...

    @overload
    def HidePart(self, Name: str) -> None:
        """Hides a part
        
        Args:
            Name: Name of part to hide
        """
        ...

    @overload
    def HidePart(self, Part: AssembledPart) -> None:
        """Hides a part
        
        Args:
            Part: Part to hide
        """
        ...

    def HideSubAssembly(self, Name: str) -> None:
        """Hides a sub-assembly
        
        Args:
            Name: Name of sub-assembly to hide
        """
        ...

    @overload
    def MovePart(self, Name: str, OffsetX: float, OffsetY: float, OffsetZ: float, ApplyConstraints: bool) -> Any:
        """Moves a part
        
        Args:
            Name: Name of part to move
            OffsetX: X offset to apply
            OffsetY: Y offset to apply
            OffsetZ: Z offset to apply
            ApplyConstraints: true to apply constraints
        """
        ...

    @overload
    def MovePart(self, Part: AssembledPart, OffsetX: float, OffsetY: float, OffsetZ: float, ApplyConstraints: bool) -> Any:
        """Moves a part
        
        Args:
            Part: Part to move
            OffsetX: X offset to apply
            OffsetY: Y offset to apply
            OffsetZ: Z offset to apply
            ApplyConstraints: true to apply constraints
        """
        ...

    def MoveParts(self, Names: List, OffsetX: float, OffsetY: float, OffsetZ: float, ApplyConstraints: bool) -> Any:
        """Moves a set of parts
        
        Args:
            Names: Names of parts to move
            OffsetX: X offset to apply
            OffsetY: Y offset to apply
            OffsetZ: Z offset to apply
            ApplyConstraints: true to apply constraints
        """
        ...

    def MoveSubAssemblies(self, Names: List, OffsetX: float, OffsetY: float, OffsetZ: float, ApplyConstraints: bool) -> Any:
        """Moves a set of sub-assemblies
        
        Args:
            Names: Names of sub-assemblies to move
            OffsetX: X offset to apply
            OffsetY: Y offset to apply
            OffsetZ: Z offset to apply
            ApplyConstraints: true to apply constraints
        """
        ...

    @overload
    def MoveSubAssembly(self, Name: str, OffsetX: float, OffsetY: float, OffsetZ: float, ApplyConstraints: bool) -> Any:
        """Moves a sub-assembly
        
        Args:
            Name: Name of sub-assembly to move
            OffsetX: X offset to apply
            OffsetY: Y offset to apply
            OffsetZ: Z offset to apply
            ApplyConstraints: true to apply constraints
        """
        ...

    @overload
    def MoveSubAssembly(self, SubAssembly: AssembledSubAssembly, OffsetX: float, OffsetY: float, OffsetZ: float, ApplyConstraints: bool) -> Any:
        """Moves a sub-assembly
        
        Args:
            SubAssembly: Sub-assembly to move
            OffsetX: X offset to apply
            OffsetY: Y offset to apply
            OffsetZ: Z offset to apply
            ApplyConstraints: true to apply constraints
        """
        ...

    def PauseUpdating(self) -> Any:
        """Pauses updating the assembly user interface
        """
        ...

    def Regenerate(self) -> Any:
        """Regenerates the assembly
        """
        ...

    def ResumeUpdating(self) -> Any:
        """Resumes updating the assembly user interface
        """
        ...

    @overload
    def RotatePart(self, Name: str, AngleX: float, AngleY: float, AngleZ: float, ApplyConstraints: bool) -> Any:
        """Rotates a part
        
        Args:
            Name: Name of part to rotate
            AngleX: X rotation angle in degrees
            AngleY: Y rotation angle in degrees
            AngleZ: Z rotation angle in degrees
            ApplyConstraints: true to apply constraints
        """
        ...

    @overload
    def RotatePart(self, Part: AssembledPart, AngleX: float, AngleY: float, AngleZ: float, ApplyConstraints: bool) -> Any:
        """Rotates a part
        
        Args:
            Part: Part to rotate
            AngleX: X rotation angle in degrees
            AngleY: Y rotation angle in degrees
            AngleZ: Z rotation angle in degrees
            ApplyConstraints: true to apply constraints
        """
        ...

    def RotateParts(self, Names: List, AngleX: float, AngleY: float, AngleZ: float, ApplyConstraints: bool) -> Any:
        """Rotates a set of parts
        
        Args:
            Names: Names of parts to rotate
            AngleX: X rotation angle in degrees
            AngleY: Y rotation angle in degrees
            AngleZ: Z rotation angle in degrees
            ApplyConstraints: true to apply constraints
        """
        ...

    def RotateSubAssemblies(self, Names: List, AngleX: float, AngleY: float, AngleZ: float, ApplyConstraints: bool) -> Any:
        """Rotates a set of sub-assemblies
        
        Args:
            Names: Names of sub-assemblies to rotate
            AngleX: X rotation angle in degrees
            AngleY: Y rotation angle in degrees
            AngleZ: Z rotation angle in degrees
            ApplyConstraints: true to apply constraints
        """
        ...

    @overload
    def RotateSubAssembly(self, Name: str, AngleX: float, AngleY: float, AngleZ: float, ApplyConstraints: bool) -> Any:
        """Rotates a sub-assembly
        
        Args:
            Name: Name of sub-assembly to rotate
            AngleX: X rotation angle in degrees
            AngleY: Y rotation angle in degrees
            AngleZ: Z rotation angle in degrees
            ApplyConstraints: true to apply constraints
        """
        ...

    @overload
    def RotateSubAssembly(self, SubAssembly: AssembledSubAssembly, AngleX: float, AngleY: float, AngleZ: float, ApplyConstraints: bool) -> Any:
        """Rotates a sub-assembly
        
        Args:
            SubAssembly: Sub-assembly to rotate
            AngleX: X rotation angle in degrees
            AngleY: Y rotation angle in degrees
            AngleZ: Z rotation angle in degrees
            ApplyConstraints: true to apply constraints
        """
        ...

    @overload
    def RotateSubAssembly(self, AssemOcc: IADOccurrence, AngleX: float, AngleY: float, AngleZ: float, ApplyConstraints: bool) -> Any:
        """Rotates a sub-assembly
        
        Args:
            AssemOcc: Occurence of sub-assembly to rotate
            AngleX: X rotation angle in degrees
            AngleY: Y rotation angle in degrees
            AngleZ: Z rotation angle in degrees
            ApplyConstraints: true to apply constraints
        """
        ...

    @overload
    def Save(self) -> None:
        """Saves the assembly using the current path and file name
        """
        ...

    @overload
    def Save(self, Folder: str) -> None:
        """Saves the assembly to a specific folder
        
        Args:
            Folder: Folder to save to
        """
        ...

    def SaveAll(self, Folder: str) -> None:
        """Save the assembly and all parts/sub-assemblies to a folder
        
        Args:
            Folder: Folder to save to
        """
        ...

    def SaveAs(self, Folder: str, NewName: str) -> None:
        """Saves the assembly to a specific folder with a new name
        
        Args:
            Folder: Folder to save to
            NewName: New name for assembly
        """
        ...

    def SaveSnapshot(self, FileName: str, Width: int, Height: int, UseAspectRatio: bool, UseWidthandHeight: bool) -> None:
        """Saves the current view as a bitmap image
        
        Args:
            FileName: Path and mame of file to save to
            Width: Width in pixels
            Height: Height in pixels
            UseAspectRatio: if true uses greater of width/height along with current aspect ratio
            UseWidthandHeight: if true uses current width/height of view
        """
        ...

    def SaveThumbnail(self, FileName: str, Width: int, Height: int) -> None:
        """Saves a thumbnail image of the assembly
        
        Args:
            FileName: Path and name of file to save to
            Width: Width of thumbnail in pixels
            Height: Height of thumbnail in pixels
        """
        ...

    def SetCustomProperty(self, Name: str, Value: str) -> Any:
        """Sets the value of a custom property
            The custom property must already be defined on the assembly or defined on the user's PC
        
        Args:
            Name: Name of the custom property
            Value: New value for the custom property
        """
        ...

    def SetUserData(self, Name: str, Dict: PythonDictionary) -> Any:
        """Sets user data
        
        Args:
            Name: Data name of the format companyname.projectname.dataname
            Dict: Python dictionary of data to store
        """
        ...

    @overload
    def ShowPart(self, Name: str) -> None:
        """Shows a part
        
        Args:
            Name: Name of part to show
        """
        ...

    @overload
    def ShowPart(self, Part: AssembledPart) -> None:
        """Shows a part
        
        Args:
            Part: Part to show
        """
        ...

    def ShowSubAssembly(self, Name: str) -> None:
        """Shows a sub-assembly
        
        Args:
            Name: Name of sub-assembly to show
        """
        ...

    @overload
    def SuppressPart(self, Name: str) -> Any:
        """Suppresses a part
        
        Args:
            Name: Name of part to suppress
        """
        ...

    @overload
    def SuppressPart(self, Part: AssembledPart) -> Any:
        """Suppresses a part
        
        Args:
            Part: Part to suppress
        """
        ...

    def SuppressSubAssembly(self, Name: str) -> Any:
        """Suppresses a sub-assembly
        
        Args:
            Name: Name of sub-assembly to suppress
        """
        ...

    @overload
    def UnanchorPart(self, Name: str) -> Any:
        """Un-anchors a part
        
        Args:
            Name: Name of part to un-anchor
        """
        ...

    @overload
    def UnanchorPart(self, Part: AssembledPart) -> Any:
        """Un-anchors a part
        
        Args:
            Part: Part to un-anchor
        """
        ...

    def UnanchorSubAssembly(self, Name: str) -> Any:
        """Un-anchors a sub-assembly
        
        Args:
            Name: Name of sub-assembly to un-anchor
        """
        ...

    @overload
    def UnsuppressPart(self, Name: str) -> Any:
        """Un-suppresses a part
        
        Args:
            Name: Name of part to un-suppress
        """
        ...

    @overload
    def UnsuppressPart(self, Part: AssembledPart) -> Any:
        """Un-suppresses a part
        
        Args:
            Part: Part to un-suppress
        """
        ...

    def UnsuppressSubAssembly(self, Name: str) -> Any:
        """Un-suppresses a sub-assembly
        
        Args:
            Name: Name of sub-assembly to un-suppress
        """
        ...

    # Enums and Constants
    class ConstraintBoundsType:
        """Assembly constraint bounds types"""
        pass
