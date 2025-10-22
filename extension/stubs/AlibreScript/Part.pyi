"""Auto-generated Python 3 stub file for AlibreScript API

This file provides type hints and documentation for the AlibreScript API.
Compatible with Python 3.6+ and modern IDEs with type checking support.
"""

from __future__ import annotations
from typing import Any, List, Union, TYPE_CHECKING
from typing import overload

if TYPE_CHECKING:
    from AlibreScript.Axis import Axis
    from AlibreScript.Configuration import Configuration
    from AlibreScript.Edge import Edge
    from AlibreScript.Face import Face
    from AlibreScript.Feature import Feature
    from AlibreScript.Parameter import Parameter
    from AlibreScript.Plane import Plane
    from AlibreScript.Point import Point
    from AlibreScript.Sketch import Sketch
    from AlibreScript.Sketch3D import Sketch3D
    from AlibreScript.Vertex import Vertex


class Part:

    @overload
    def __init__(self, folder: str, name: str) -> None:
        """Opens an existing part

        Args:
            folder: Folder containing part
            name: Name of part to open
        """
        ...

    @overload
    def __init__(self, folder: str, name: str, hide_editor: bool) -> None:
        """Opens an existing part, optionally hiding the editor

        Args:
            folder: Folder containing part
            name: Name of part to open
            hide_editor: True to hide the editor (only valid if part is not already open)
        """
        ...

    @overload
    def __init__(self, name: str) -> None:
        """Creates a new part

        Args:
            name: Name of new part
        """
        ...

    @overload
    def __init__(self, name: str, create_new: bool) -> None:
        """Creates a new part or accesses an already opened part

        Args:
            name: Name of part to create or access
            create_new: True to create a new part, false to access an opened part
        """
        ...

    @overload
    def __init__(self, name: str, create_new: bool, hide_editor: bool) -> None:
        """Creates a new part or accesses an already opened part, optionally hiding the editor

        Args:
            name: Name of part to create or access
            create_new: True to create a new part, false to access an opened part
            hide_editor: True to hide the editor (only valid if CreateNew is true)
        """
        ...

    @overload
    def __init__(self, file_name: str, type: Any) -> None:
        """Opens or imports an existing file for editing

        Args:
            file_name: Name of file to open
            type: Type of file (Part.FileTypes: GeomagicDesignPart, STEP, IGES, ThreeDM, SAT, STL_in, STL_cm, STL_mm)
        """
        ...

    @overload
    def __init__(self, file_name: str, type: Any, hide_editor: bool) -> None:
        """Opens or imports an existing file for editing, optionally hiding the editor

        Args:
            file_name: Name of file to open
            type: Type of file (Part.FileTypes: GeomagicDesignPart, STEP, IGES, ThreeDM, SAT, STL_in, STL_cm, STL_mm)
            hide_editor: True to hide the editor
        """
        ...

    # Properties (read-only attributes set by Alibre at runtime)
    Comment: Any  # Comment property
    Configurations: Any  # List of configurations defined on the part
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
    FileName: Any  # Path and filename of the part
    Keywords: Any  # Keywords property
    LastAuthor: Any  # Last Author property
    LastUpdateDate: Any  # Last Update Date property
    ManufacturingApprovedBy: Any  # Manufacturing Approved By property
    ManufacturingApprovedDate: Any  # Product property
    Mass: Any  # Mass of the part
    Material: Any  # Material of the part
    ModifiedInformation: Any  # Modified Information property
    Name: Any  # Name of the part
    Number: Any  # User-defined number for the part
    Origin: Any  # Gets the origin (language independent)
    Parameters: Any  # List of parameters defined on the part
    Product: Any  # Product property
    ReceivedFrom: Any  # Received From property
    Revision: Any  # Revision property
    Selections: Any  # Gets the currently selected items as [ItemA, ItemB, ...]             Supports faces, edges, vertices, planes, axes and points
    StockSize: Any  # Stock Size property
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

    def Add3DSketch(self, Name: str) -> Sketch3D:
        """Creates a new 3D sketch
        
        Args:
            Name: Name of sketch
        
        Returns:
            Created sketch
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
    def AddAxis(self, Name: str, PointA: Point, PointB: Point) -> Axis:
        """Creates an axis based on two points
        
        Args:
            Name: Name of axis
            PointA: First point object
            PointB: Second point object
        
        Returns:
            New axis
        """
        ...

    @overload
    def AddAxis(self, Name: str, CylindricalFace: Face) -> Axis:
        """Creates an axis for a cylindrical face
        
        Args:
            Name: Name of axis
            CylindricalFace: Cylindrical face
        
        Returns:
            New axis
        """
        ...

    @overload
    def AddAxis(self, Name: str, Point1: List, Point2: List) -> Axis:
        """Creates an axis based on two points
        
        Args:
            Name: Name of axis
            Point1: First point [X, Y, Z]
            Point2: Second point [X, Y, Z]
        
        Returns:
            New axis
        """
        ...

    @overload
    def AddChamfer(self, Name: str, Item: IChamferable, Distance1: float, Distance2: float, TangentPropagate: bool) -> Feature:
        """Adds a chamfer to a face or edge
        
        Args:
            Name: Name of chamfer
            Item: Face or edge to chamfer
            Distance1: First chamfer distance
            Distance2: Second chamfer distance
            TangentPropagate: True to propagate the chamfer along connected edges
        
        Returns:
            Chamfer feature
        """
        ...

    @overload
    def AddChamfer(self, Name: str, Items: List, Distance1: float, Distance2: float, TangentPropagate: bool) -> Feature:
        """Adds a chamfer to a set of faces and edges
        
        Args:
            Name: Name of chamfer
            Items: Faces and edges to chamfer
            Distance1: First chamfer distance
            Distance2: Second chamfer distance
            TangentPropagate: True to propagate the chamfer along connected edges
        
        Returns:
            Chamfer feature
        """
        ...

    @overload
    def AddChamfer(self, Name: str, Item: IChamferable, Distance: float, TangentPropagate: bool) -> Feature:
        """Adds a chamfer to a face or edge
        
        Args:
            Name: Name of chamfer
            Item: Face or edge to chamfer
            Distance: Chamfer distance
            TangentPropagate: True to propagate the chamfer along connected edges
        
        Returns:
            Chamfer feature
        """
        ...

    @overload
    def AddChamfer(self, Name: str, Items: List, Distance: float, TangentPropagate: bool) -> Feature:
        """Adds a chamfer to a set of faces and edges
        
        Args:
            Name: Name of chamfer
            Items: Faces and edges to chamfer
            Distance: Chamfer distance
            TangentPropagate: True to propagate the chamfer along connected edges
        
        Returns:
            Chamfer feature
        """
        ...

    @overload
    def AddChamferAngle(self, Name: str, Item: IChamferable, Distance: float, Angle: float, TangentPropagate: bool) -> Feature:
        """Adds a chamfer to a face or edge
        
        Args:
            Name: Name of chamfer
            Item: Face or edge to chamfer
            Distance: Chamfer distance
            Angle: Chamfer angle
            TangentPropagate: True to propagate the chamfer along connected edges
        
        Returns:
            Chamfer feature
        """
        ...

    @overload
    def AddChamferAngle(self, Name: str, Items: List, Distance: float, Angle: float, TangentPropagate: bool) -> Feature:
        """Adds a chamfer to a set of faces and edges
        
        Args:
            Name: Name of chamfer
            Items: Faces and edges to chamfer
            Distance: Chamfer distance
            Angle: Chamfer angle
            TangentPropagate: True to propagate the chamfer along connected edges
        
        Returns:
            Chamfer feature
        """
        ...

    @overload
    def AddConfiguration(self, Name: str) -> Configuration:
        """Adds a configuration to the part
        
        Args:
            Name: Name of configuration
        
        Returns:
            New configuration
        """
        ...

    @overload
    def AddConfiguration(self, Name: str, BaseConfigurationName: str) -> Configuration:
        """Adds a configuration to the part using another configuration as a base
        
        Args:
            Name: Name of configuration
            BaseConfigurationName: Name of base configuration to use
        
        Returns:
            New configuration
        """
        ...

    @overload
    def AddExtrudeBoss(self, Name: str, Sketch: Sketch, Depth: float, IsReversed: bool) -> Feature:
        """Adds a simple extrude boss to a specific depth
        
        Args:
            Name: Name of extrusion
            Sketch: Sketch to extrude
            Depth: Extrusion distance
            IsReversed: True if extrusion direction is reversed
        
        Returns:
            Extruded feature
        """
        ...

    @overload
    def AddExtrudeBoss(self, Name: str, Sketch: Sketch, Depth: float, IsReversed: bool, EndCondition: EndCondition, EndPlane: ISketchSurface, EndOffset: float, Direction: DirectionType, SweepPath: ISweepPath, DraftAngle: float, OutwardDraft: bool) -> Feature:
        """Adds an extrude feature
        
        Args:
            Name: Name of extrusion
            Sketch: Sketch to extrude
            Depth: Depth of extrusion
            IsReversed: true if direction is reversed
            EndCondition: End condition for extrusion
            EndPlane: Face or plane to terminate extrusion
            EndOffset: Offset from face or plane to terminate extrusion
            Direction: Direction of extrusion
            SweepPath: Sketch or edge to follow when extruding
            DraftAngle: Angle of draft
            OutwardDraft: true if outward draft
        
        Returns:
            Extruded feature
        """
        ...

    @overload
    def AddExtrudeCut(self, Name: str, Sketch: Sketch, Depth: float, IsReversed: bool) -> Feature:
        """Adds a simple extrude cut to a specific depth
        
        Args:
            Name: Name of extrusion
            Sketch: Sketch to extrude
            Depth: Extrusion distance
            IsReversed: True if extrusion direction is reversed
        
        Returns:
            Extruded feature
        """
        ...

    @overload
    def AddExtrudeCut(self, Name: str, Sketch: Sketch, Depth: float, IsReversed: bool, EndCondition: EndCondition, EndPlane: ISketchSurface, EndOffset: float, Direction: DirectionType, SweepPath: ISweepPath, DraftAngle: float, OutwardDraft: bool) -> Feature:
        """Adds an extrude cut feature
        
        Args:
            Name: Name of extrusion
            Sketch: Sketch to extrude
            Depth: Depth of extrusion
            IsReversed: true if direction is reversed
            EndCondition: End condition for extrusion
            EndPlane: Face or plane to terminate extrusion
            EndOffset: Offset from face or plane to terminate extrusion
            Direction: Direction of extrusion
            SweepPath: Sketch or edge to follow when extruding
            DraftAngle: Angle of draft
            OutwardDraft: true if outward draft
        
        Returns:
            Extruded feature
        """
        ...

    @overload
    def AddFillet(self, Name: str, Item: IFilletable, Radius: float, TangentPropagate: bool) -> Feature:
        """Adds a constant radius fillet to a face or edge
        
        Args:
            Name: Name of fillet
            Item: Face or edge to fillet
            Radius: Radius of fillet
            TangentPropagate: True to propagate the fillet along connected edges
        
        Returns:
            Fillet feature
        """
        ...

    @overload
    def AddFillet(self, Name: str, Items: List, Radius: float, TangentPropagate: bool) -> Feature:
        """Adds a constant radius fillet to a set of faces and edges
        
        Args:
            Name: Name of fillet
            Items: Faces and edges to fillet
            Radius: Radius of fillet
            TangentPropagate: True to propagate the fillet along connected edges
        
        Returns:
            Fillet feature
        """
        ...

    @overload
    def AddFillet(self, Name: str, Items: List, StartRadii: List, EndRadii: List, TangentPropagate: bool) -> Feature:
        """Adds a variable radius fillet to a set of faces and edges
        
        Args:
            Name: Name of fillet
            Items: Faces and edges to fillet
            StartRadii: Start radii of fillets
            EndRadii: End radii of fillets
            TangentPropagate: True to propagate the fillet along connected edges
        
        Returns:
            Fillet feature
        """
        ...

    def AddGear(self, Name: str, NumberofTeeth: float, PitchDiameter: int, PressureAngle: float, DiametralPitch: float, SingleTooth: bool, CenterX: float, CenterY: float, InvolutePoints: int, Plane: ISketchSurface) -> Any:
        """Adds a gear sketch to the part
        
        Args:
            Name: Name of gear sketch
            NumberofTeeth: Number of teeth
            PitchDiameter: Diameter of pitch circle in current units
            PressureAngle: Pressure angle (14.5 is typical)
            DiametralPitch: Diametral angle (tooth size) (25.4/module) in teeth per inch
            SingleTooth: true to create only a single tooth profile
            CenterX: X-coordinate of gear center
            CenterY: Y-coordinate of gear center
            InvolutePoints: Number of points for involute curve. Decreasing this makes Cubify/Geomagic faster. Increasing makes tooth profiles more accurate and allows gears with more teeth to be generated.
            Plane: Plane or face to create gear sketch on
        
        Returns:
            Gear sketch
        """
        ...

    @overload
    def AddGearDN(self, Name: str, NumberofTeeth: float, PressureAngle: int, DiametralPitch: float, CenterX: float, CenterY: float, Plane: ISketchSurface) -> Any:
        """Adds a gear sketch to the part using diametral pitch and number of teeth
        
        Args:
            Name: Name of gear sketch
            NumberofTeeth: Number of teeth
            PressureAngle: Pressure angle (14.5 is typical)
            DiametralPitch: Diametral angle (tooth size) (1/module)
            CenterX: X-coordinate of center of gear
            CenterY: Y-coordinate of center of gear
            Plane: Plane or face to create gear sketch on
        
        Returns:
            Gear sketch
        """
        ...

    @overload
    def AddGearDN(self, Name: str, NumberofTeeth: float, PressureAngle: int, DiametralPitch: float, CenterX: float, CenterY: float, SingleTooth: bool, Plane: ISketchSurface) -> Any:
        """Adds a gear sketch to the part using diametral pitch and number of teeth
        
        Args:
            Name: Name of gear sketch
            NumberofTeeth: Number of teeth
            PressureAngle: Pressure angle (14.5 is typical)
            DiametralPitch: Diametral angle (tooth size) (1/module)
            CenterX: X-coordinate of center of gear
            CenterY: Y-coordinate of center of gear
            SingleTooth: True to generate a single tooth
            Plane: Plane or face to create gear sketch on
        
        Returns:
            Gear sketch
        """
        ...

    @overload
    def AddGearDP(self, Name: str, PitchDiameter: float, PressureAngle: float, DiametralPitch: float, CenterX: float, CenterY: float, Plane: ISketchSurface) -> Any:
        """Adds a gear sketch to the part using diametral pitch and pitch diameter
        
        Args:
            Name: Name of gear sketch
            PitchDiameter: Diameter of pitch circle
            PressureAngle: Pressure angle (14.5 is typical)
            DiametralPitch: Diametral angle (tooth size) (1/module)
            CenterX: X-coordinate of center of gear
            CenterY: Y-coordinate of center of gear
            Plane: Plane or face to create gear sketch on
        
        Returns:
            Gear sketch
        """
        ...

    @overload
    def AddGearDP(self, Name: str, PitchDiameter: float, PressureAngle: float, DiametralPitch: float, CenterX: float, CenterY: float, SingleTooth: bool, Plane: ISketchSurface) -> Any:
        """Adds a gear sketch to the part using diametral pitch and pitch diameter
        
        Args:
            Name: Name of gear sketch
            PitchDiameter: Diameter of pitch circle
            PressureAngle: Pressure angle (14.5 is typical)
            DiametralPitch: Diametral angle (tooth size) (1/module)
            CenterX: X-coordinate of center of gear
            CenterY: Y-coordinate of center of gear
            SingleTooth: True to generate a single tooth
            Plane: Plane or face to create gear sketch on
        
        Returns:
            Gear sketch
        """
        ...

    @overload
    def AddGearNP(self, Name: str, NumberofTeeth: int, PitchDiameter: float, PressureAngle: float, CenterX: float, CenterY: float, Plane: ISketchSurface) -> Any:
        """Adds a gear sketch to the part using number of teeth and pitch diameter
        
        Args:
            Name: Name of gear sketch
            NumberofTeeth: Number of teeth
            PitchDiameter: Diameter of pitch circle
            PressureAngle: Pressure angle (14.5 is typical)
            CenterX: X-coordinate of center of gear
            CenterY: Y-coordinate of center of gear
            Plane: Plane or face to create gear sketch on
        
        Returns:
            Gear sketch
        """
        ...

    @overload
    def AddGearNP(self, Name: str, NumberofTeeth: int, PitchDiameter: float, PressureAngle: float, CenterX: float, CenterY: float, SingleTooth: bool, Plane: ISketchSurface) -> Any:
        """Adds a gear sketch to the part using number of teeth and pitch diameter
        
        Args:
            Name: Name of gear sketch
            NumberofTeeth: Number of teeth
            PitchDiameter: Diameter of pitch circle
            PressureAngle: Pressure angle (14.5 is typical)
            CenterX: X-coordinate of center of gear
            CenterY: Y-coordinate of center of gear
            SingleTooth: True to generate a single tooth
            Plane: Plane or face to create gear sketch on
        
        Returns:
            Gear sketch
        """
        ...

    @overload
    def AddLoftBoss(self, Name: str, CrossSections: List[Union[Face, Sketch, Point]], MinimizeTwist: bool, MinimizeCurvature: bool, SimplifySurface: bool, ConnectEnds: bool) -> Feature:
        """Adds a loft extrusion
        
        Args:
            Name: Name of loft
            CrossSections: Python list of cross sections (faces, 2D sketches, design points)
            MinimizeTwist: True to minimize twist
            MinimizeCurvature: True to minimize curvature
            SimplifySurface: True to simplify the loft surface
            ConnectEnds: True to connect the start of the loft with the end
        
        Returns:
            Extruded feature
        """
        ...

    @overload
    def AddLoftBoss(self, Name: str, CrossSections: List[Union[Face, Sketch, Point]], GuideCurves: List[Sketch], GuideType: GuideCurveTypes, MinimizeTwist: bool, MinimizeCurvature: bool, SimplifySurface: bool, ConnectEnds: bool) -> Feature:
        """Adds a loft extrusion using guide curves
        
        Args:
            Name: Name of loft
            CrossSections: Python list of cross sections (faces, 2D sketches, design points)
            GuideCurves: Python list of guide curves (3D sketches)
            GuideType: Type of guide curve
            MinimizeTwist: True to minimize twist
            MinimizeCurvature: True to minimize curvature
            SimplifySurface: True to simplify the loft surface
            ConnectEnds: True to connect the start of the loft with the end
        
        Returns:
            Extruded feature
        """
        ...

    @overload
    def AddLoftCut(self, Name: str, CrossSections: List[Union[Face, Sketch, Point]], MinimizeTwist: bool, MinimizeCurvature: bool, SimplifySurface: bool, ConnectEnds: bool) -> Feature:
        """Adds a loft cut
        
        Args:
            Name: Name of loft
            CrossSections: Python list of cross sections (faces, 2D sketches, design points)
            MinimizeTwist: True to minimize twist
            MinimizeCurvature: True to minimize curvature
            SimplifySurface: True to simplify the loft surface
            ConnectEnds: True to connect the start of the loft with the end
        
        Returns:
            Cut feature
        """
        ...

    @overload
    def AddLoftCut(self, Name: str, CrossSections: List[Union[Face, Sketch, Point]], GuideCurves: List[Sketch], GuideType: GuideCurveTypes, MinimizeTwist: bool, MinimizeCurvature: bool, SimplifySurface: bool, ConnectEnds: bool) -> Feature:
        """Adds a loft cut using guide curves
        
        Args:
            Name: Name of loft
            CrossSections: Python list of cross sections (faces, 2D sketches, design points)
            GuideCurves: Python list of guide curves (3D sketches)
            GuideType: Type of guide curve
            MinimizeTwist: True to minimize twist
            MinimizeCurvature: True to minimize curvature
            SimplifySurface: True to simplify the loft surface
            ConnectEnds: True to connect the start of the loft with the end
        
        Returns:
            Extruded feature
        """
        ...

    @overload
    def AddParameter(self, Name: str, Type: ParameterTypes, Value: float) -> Parameter:
        """Adds a cm/mm/in/deg parameter to the part
        
        Args:
            Name: Name of parameter
            Type: Type of parameter
            Value: Value for parameter
        
        Returns:
            New parameter
        """
        ...

    @overload
    def AddParameter(self, Name: str, Type: ParameterTypes, UnitstoUse: ParameterUnits, Value: float) -> Parameter:
        """Adds a parameter to the part with specific units
        
        Args:
            Name: Name of parameter
            Type: Type of parameter
            UnitstoUse: Units to use
            Value: Value for parameter
        
        Returns:
            New parameter
        """
        ...

    @overload
    def AddParameter(self, Name: str, Type: ParameterTypes, Equation: str) -> Parameter:
        """Adds a parameter to the part
        
        Args:
            Name: Name of parameter
            Type: Type of parameter
            Equation: Equation for parameter
        
        Returns:
            New parameter
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
    def AddPlane(self, Name: str, Axis: Axis, Point: Point) -> Plane:
        """Creates a new plane contaning an axis and a point
        
        Args:
            Name: Name of new plane
            Axis: Axis that lies on plane
            Point: Point that lies on plane
        
        Returns:
            New plane
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
        """Creates a plane using three points. Each point is defined as list of [x, y, z]
        
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
    def AddPoint(self, Name: str, Point: List) -> Point:
        """Adds a point to the part
        
        Args:
            Name: Name of the new point
            Point: Point location [x, y, z]
        
        Returns:
            The new point
        """
        ...

    @overload
    def AddPoint(self, Name: str, Point: Point) -> Point:
        """Adds a point to the part
        
        Args:
            Name: Name of the point
            Point: Point to add
        """
        ...

    @overload
    def AddPoint(self, Name: str, X: float, Y: float, Z: float) -> Point:
        """Adds a point to the part
        
        Args:
            Name: Name of new point
            X: X coordinate
            Y: Y coordinate
            Z: Z coordinate
        
        Returns:
            The new point
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

    def AddRevolveBoss(self, Name: str, Sketch: Sketch, Axis: Axis, Angle: float) -> Feature:
        """Creates a revolve boss feature
        
        Args:
            Name: Name of feature
            Sketch: Sketch to revolve
            Axis: Axis to rotate around
            Angle: Rotation angle in degrees
        
        Returns:
            Created feature
        """
        ...

    def AddRevolveCut(self, Name: str, Sketch: Sketch, Axis: Axis, Angle: float) -> Feature:
        """Creates a revolve cut feature
        
        Args:
            Name: Name of feature
            Sketch: Sketch to revolve
            Axis: Axis to rotate around
            Angle: Rotation angle in degrees
        
        Returns:
            Created feature
        """
        ...

    def AddSketch(self, Name: str, Plane: ISketchSurface) -> Sketch:
        """Creates a new sketch using a plane/face
        
        Args:
            Name: Name of sketch
            Plane: Plane/face to use for sketch
        
        Returns:
            Created sketch
        """
        ...

    def AddSweepBoss(self, Name: str, ProfileSketch: Sketch, PathSketch: ISweepPath, IsRigid: bool, EndCondition: EndCondition, EndPlane: ISketchSurface, EndOffset: float, DraftAngle: float, OutwardDraft: bool) -> Feature:
        """Adds a sweep extrude feature
        
        Args:
            Name: Name of extrusion
            ProfileSketch: Sketch to extrude
            PathSketch: Sketch or edge to sweep along
            IsRigid: true if path is parallel to profile
            EndCondition: End condition for extrusion
            EndPlane: Face or plane to terminate extrusion
            EndOffset: Offset from face or plane to terminate extrusion
            DraftAngle: Angle of draft
            OutwardDraft: true if outward draft
        
        Returns:
            Extruded feature
        """
        ...

    def AddSweepCut(self, Name: str, ProfileSketch: Sketch, PathSketch: ISweepPath, IsRigid: bool, EndCondition: EndCondition, EndPlane: ISketchSurface, EndOffset: float, DraftAngle: float, OutwardDraft: bool) -> Feature:
        """Adds a sweep extrude cut feature
        
        Args:
            Name: Name of extrusion
            ProfileSketch: Sketch to extrude
            PathSketch: Sketch or edge to sweep along
            IsRigid: true if path is parallel to profile
            EndCondition: End condition for extrusion
            EndPlane: Face or plane to terminate extrusion
            EndOffset: Offset from face or plane to terminate extrusion
            DraftAngle: Angle of draft
            OutwardDraft: true if outward draft
        
        Returns:
            Extruded feature
        """
        ...

    @overload
    def AddVertexChamfer(self, Name: str, Item: Vertex, Distance1: float, Distance2: float, Distance3: float) -> Feature:
        """Adds a chamfer to a vertex
        
        Args:
            Name: Name of chamfer
            Item: Vertex to chamfer
            Distance1: First chamfer distance
            Distance2: Second chamfer distance
            Distance3: Third chamfer distance
        
        Returns:
            Chamfer feature
        """
        ...

    @overload
    def AddVertexChamfer(self, Name: str, Items: List, Distance1: float, Distance2: float, Distance3: float) -> Feature:
        """Adds a chamfer to a set of vertices
        
        Args:
            Name: Name of chamfer
            Items: Vertices to chamfer
            Distance1: First chamfer distance
            Distance2: Second chamfer distance
            Distance3: Third chamfer distance
        
        Returns:
            Chamfer feature
        """
        ...

    def Close(self) -> None:
        """Closes the part
            If it is unsaved then changes will be lost
        """
        ...

    def DisplayUnits(self) -> Any:
        """Gets the display units for the part
        
        Returns:
            The display units
        """
        ...

    def ExportBIP(self, FileName: str) -> Any:
        """Exports a keyshot file
        
        Args:
            FileName: Path and name of keyshot file
        """
        ...

    def ExportIGES(self, FileName: str) -> Any:
        """Exports the part as a IGES file
        
        Args:
            FileName: Path and name of IGES file
        """
        ...

    def ExportRotatedSTL(self, FileName: str, BottomFace: Face, ForcetoMillimeters: bool, UseCustomSettings: bool, MaxCellSize: float, NormalDeviation: float, SurfaceDeviation: float) -> Any:
        """Exports the part as an STL rotated so that a specific face is on the bottom
        
        Args:
            FileName: Path and name of STL file
            BottomFace: Face to use as bottom of part
            ForcetoMillimeters: true to output STL in millimeters regardless of part units
            UseCustomSettings: true to use custom STL settings, false to use settings in system properties
            MaxCellSize: Custom max cell size
            NormalDeviation: Custom normal deviation
            SurfaceDeviation: Custom surface deviation
        """
        ...

    def ExportSAT(self, FileName: str, Version: int, SaveColors: bool) -> Any:
        """Exports the part as a SAT file
        
        Args:
            FileName: Path and name of SAT file
            Version: Exported SAT file version
            SaveColors: true to preseve colors
        """
        ...

    def ExportSTEP203(self, FileName: str) -> Any:
        """Exports the part as a STEP 203 file
        
        Args:
            FileName: Path and name of STEP 203 file
        """
        ...

    def ExportSTEP214(self, FileName: str) -> Any:
        """Exports the part as a STEP 214 file
        
        Args:
            FileName: Path and name of STEP 214 file
        """
        ...

    def ExportSTL(self, FileName: str) -> Any:
        """Exports the part as an STL file
        
        Args:
            FileName: Path and name of STL file
        """
        ...

    def Get3DSketch(self, Name: str) -> Sketch3D:
        """Gets a sketch using the name of the sketch
        
        Args:
            Name: Name of sketch
        
        Returns:
            Sketch object
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

    def GetBoundingBox(self) -> Any:
        """Gets the bounding box for the part as eight points
        
        Returns:
            Python list of eight points as [P1, P2, ... P8]. Each point is [X, Y, Z]
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

    def GetFeature(self, Name: str) -> Feature:
        """Gets a feature on the part
        
        Args:
            Name: Name of the feature to get
        
        Returns:
            The feature or null if not found
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

    def GetPlane(self, Name: str) -> Plane:
        """Gets a plane using the name of the plane
        
        Args:
            Name: Name of plane to find
        
        Returns:
            The plane
        """
        ...

    def GetPoint(self, Name: str) -> Point:
        """Gets a point on the part using the point name. The point must have been created in a script
        
        Args:
            Name: Name of point to get
        
        Returns:
            Point on the part
        """
        ...

    def GetSelectionAssembly(self) -> Assembly:
        """The assembly that the part was selected on
            Only valid when a selection has been made
        
        Returns:
            Assembly or null for no assembly
        """
        ...

    def GetSketch(self, Name: str) -> Sketch:
        """Gets a sketch using the name of the sketch
        
        Args:
            Name: Name of sketch
        
        Returns:
            Sketch object
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

    def GetVertex(self, Name: str) -> Vertex:
        """Gets a vertex using it's name "Vertex<n>"
        
        Args:
            Name: Name of vertex
        
        Returns:
            Vertex if found
        """
        ...

    def GetVertices(self) -> List[Vertex]:
        """Gets a python list of the current vertices in the part
        
        Returns:
            Python list of vertices
        """
        ...

    @overload
    def HideFeature(self, Name: str) -> None:
        """Hides a feature on the part
        
        Args:
            Name: Name of the feature to hide
        """
        ...

    @overload
    def HideFeature(self, Feature: Feature) -> None:
        """Hides a feature on the part
        
        Args:
            Feature: Feature to hide
        """
        ...

    def IsOpen(self) -> Any:
        """Checks if the part is opened
        """
        ...

    def NonUniformScale(self, Name: str, ScaleAboutCenter: bool, ScaleFactorX: float, ScaleFactorY: float, ScaleFactorZ: float) -> Any:
        """Non-uniform scaling of the part
        
        Args:
            Name: Name of the scaling
            ScaleAboutCenter: true to scale around the center of the part
            ScaleFactorX: X scale factor
            ScaleFactorY: Y scale factor
            ScaleFactorZ: Z scale factor
        
        Returns:
            Scale feature
        """
        ...

    def PauseUpdating(self) -> Any:
        """Pauses updating the part user interface
        """
        ...

    def Regenerate(self) -> Any:
        """Regenerates the part
        """
        ...

    @overload
    def RemoveFeature(self, Name: str) -> Any:
        """Removes a feature from the part
        
        Args:
            Name: Name of the feature to remove
        """
        ...

    @overload
    def RemoveFeature(self, Feature: Feature) -> Any:
        """Removes a feature from the part
        
        Args:
            Feature: Feature to remove
        """
        ...

    def RemovePlane(self, Plane: Plane) -> Any:
        """Removes a plane from the part
        
        Args:
            Plane: Plane to remove
        """
        ...

    def RemovePoint(self, Point: Point) -> Any:
        """Removes a point from the part
        
        Args:
            Point: Point to remove
        """
        ...

    @overload
    def RemoveSketch(self, Name: str) -> Any:
        """Removes a sketch from the part
        
        Args:
            Name: Name of sketch to remove
        """
        ...

    @overload
    def RemoveSketch(self, Sketch: Sketch) -> Any:
        """Removes a sketch from the part
        
        Args:
            Sketch: Sketch to remove
        """
        ...

    def ResumeUpdating(self) -> Any:
        """Resumes updating the part user interface
        """
        ...

    @overload
    def Save(self) -> None:
        """Saves the part using the current path and file name
        """
        ...

    @overload
    def Save(self, Folder: str) -> None:
        """Saves the part to a specific folder
        
        Args:
            Folder: Folder to save to
        """
        ...

    def SaveAs(self, Folder: str, NewName: str) -> None:
        """Saves the part to a specific folder with a new name
        
        Args:
            Folder: Folder to save to
            NewName: New name for part
        """
        ...

    def SaveSnapshot(self, FileName: str, Width: int, Height: int, UseAspectRatio: bool, UseWidthandHeight: bool) -> None:
        """Saves the current view as a bitmap image
        
        Args:
            FileName: Path and name of file to save to
            Width: Width in pixels
            Height: Height in pixels
            UseAspectRatio: if true uses greater of width/height along with current aspect ratio
            UseWidthandHeight: if true uses current width/height of view
        """
        ...

    def SaveThumbnail(self, FileName: str, Width: int, Height: int) -> None:
        """Saves a thumbnail image of the part
        
        Args:
            FileName: Path and name of file to save to
            Width: Width of thumbnail in pixels
            Height: Height of thumbnail in pixels
        """
        ...

    def Scale(self, Name: str, ScaleAboutCenter: bool, ScaleFactor: float) -> Any:
        """Uniform scaling of the part
        
        Args:
            Name: Name of the scaling
            ScaleAboutCenter: true to scale around the center of the part
            ScaleFactor: Scale factor
        
        Returns:
            Scale feature
        """
        ...

    @overload
    def Select(self, FaceorEdge: ISelectableGeometry) -> Any:
        """Selects a face, edge, vertex, point, axis, plane, sketch
        
        Args:
            FaceorEdge: Face, edge, vertex, point, axis plane or sketch to select
        """
        ...

    @overload
    def Select(self, FacesEdgesList: List) -> Any:
        """Selects a group of faces, edges, vertices, points, axes, planes and sketches
        
        Args:
            FacesEdgesList: List of Faces, edges, vertices, points, axes, planes and sketches to select [FaceA, FaceB, EdgeA, EdgeB, ...]
        """
        ...

    def SetColor(self, Red: int, Green: int, Blue: int) -> None:
        """Sets the color of the part
        
        Args:
            Red: Red component 0 - 255
            Green: Green component 0 - 255
            Blue: Blue component 0 - 255
        """
        ...

    def SetCustomProperty(self, Name: str, Value: str) -> Any:
        """Sets the value of a custom property
            The custom property must already be defined on the part or defined on the user's PC
        
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
    def ShowFeature(self, Name: str) -> None:
        """Shows a feature on the part
        
        Args:
            Name: Name of the feature to show
        """
        ...

    @overload
    def ShowFeature(self, Feature: Feature) -> None:
        """Shows a feature on the part
        
        Args:
            Feature: Feature to show
        """
        ...

    @overload
    def SuppressFeature(self, Name: str) -> Any:
        """Suppresses a feature on the part
        
        Args:
            Name: Name of the feature to suppress
        """
        ...

    @overload
    def SuppressFeature(self, Feature: Feature) -> Any:
        """Suppresses a feature on the part
        
        Args:
            Feature: Feature to suppress
        """
        ...

    @overload
    def UnsuppressFeature(self, Name: str) -> Any:
        """Unsuppresses a feature on the part
        
        Args:
            Name: Name of the feature to unsuppress
        """
        ...

    @overload
    def UnsuppressFeature(self, Feature: Feature) -> Any:
        """Unsuppresses a feature on the part
        
        Args:
            Feature: Feature to unsuppress
        """
        ...

    # Enums and Constants
    class DirectionType:
        """Extrusion directions - extrude along..."""
        pass

    class EndCondition:
        """Extrusion end conditions - extrude until..."""
        pass

    class FileTypes:
        """Supported file types"""
        pass
