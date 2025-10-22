"""
AlibreScript API Type Stubs

This package provides type hints and autocomplete for AlibreScript API.

Usage:
    from AlibreScript import *

    # Get current part/assembly
    MyPart = CurrentPart()
    MyAssy = CurrentAssembly()

    # Or create new
    MyPart = Part('My Part')

    # Add a sketch
    sketch = MyPart.AddSketch('Sketch1', MyPart.XYPlane)
"""

from typing import Any

# Import all classes from their respective modules
from AlibreScript.AssembledPart import AssembledPart as AssembledPart
from AlibreScript.AssembledSubAssembly import AssembledSubAssembly as AssembledSubAssembly
from AlibreScript.Assembly import Assembly as Assembly
from AlibreScript.Axis import Axis as Axis
from AlibreScript.Bspline import Bspline as Bspline
from AlibreScript.Bspline3D import Bspline3D as Bspline3D
from AlibreScript.CSharp import CSharp as CSharp
from AlibreScript.Circle import Circle as Circle
from AlibreScript.CircularArc import CircularArc as CircularArc
from AlibreScript.CircularArc3D import CircularArc3D as CircularArc3D
from AlibreScript.Configuration import Configuration as Configuration
from AlibreScript.Edge import Edge as Edge
from AlibreScript.Ellipse import Ellipse as Ellipse
from AlibreScript.EllipticalArc import EllipticalArc as EllipticalArc
from AlibreScript.Face import Face as Face
from AlibreScript.Feature import Feature as Feature
from AlibreScript.GearSketch import GearSketch as GearSketch
from AlibreScript.GlobalParameters import GlobalParameters as GlobalParameters
from AlibreScript.GuideCurveTypes import GuideCurveTypes as GuideCurveTypes
from AlibreScript.IAxis import IAxis as IAxis
from AlibreScript.IPlane import IPlane as IPlane
from AlibreScript.IPoint import IPoint as IPoint
from AlibreScript.Line import Line as Line
from AlibreScript.Line3D import Line3D as Line3D
from AlibreScript.LockTypes import LockTypes as LockTypes
from AlibreScript.Material import Material as Material
from AlibreScript.Parameter import Parameter as Parameter
from AlibreScript.ParameterTypes import ParameterTypes as ParameterTypes
from AlibreScript.ParameterUnits import ParameterUnits as ParameterUnits
from AlibreScript.Part import Part as Part
from AlibreScript.Plane import Plane as Plane
from AlibreScript.Point import Point as Point
from AlibreScript.Polyline import Polyline as Polyline
from AlibreScript.Polyline3D import Polyline3D as Polyline3D
from AlibreScript.PolylinePoint import PolylinePoint as PolylinePoint
from AlibreScript.PolylinePoint3D import PolylinePoint3D as PolylinePoint3D
from AlibreScript.Sketch import Sketch as Sketch
from AlibreScript.Sketch3D import Sketch3D as Sketch3D
from AlibreScript.SketchPoint import SketchPoint as SketchPoint
from AlibreScript.SketchPoint3D import SketchPoint3D as SketchPoint3D
from AlibreScript.ThreeD import ThreeD as ThreeD
from AlibreScript.TwoD import TwoD as TwoD
from AlibreScript.UnitTypes import UnitTypes as UnitTypes
from AlibreScript.Units import Units as Units
from AlibreScript.Vertex import Vertex as Vertex
from AlibreScript.Windows import Windows as Windows
from AlibreScript.WindowsInputTypes import WindowsInputTypes as WindowsInputTypes

__all__ = [
    'AssembledPart',
    'AssembledSubAssembly',
    'Assembly',
    'Axis',
    'Bspline',
    'Bspline3D',
    'CSharp',
    'Circle',
    'CircularArc',
    'CircularArc3D',
    'Configuration',
    'Edge',
    'Ellipse',
    'EllipticalArc',
    'Face',
    'Feature',
    'GearSketch',
    'GlobalParameters',
    'GuideCurveTypes',
    'IAxis',
    'IPlane',
    'IPoint',
    'Line',
    'Line3D',
    'LockTypes',
    'Material',
    'Parameter',
    'ParameterTypes',
    'ParameterUnits',
    'Part',
    'Plane',
    'Point',
    'Polyline',
    'Polyline3D',
    'PolylinePoint',
    'PolylinePoint3D',
    'Sketch',
    'Sketch3D',
    'SketchPoint',
    'SketchPoint3D',
    'ThreeD',
    'TwoD',
    'UnitTypes',
    'Units',
    'Vertex',
    'Windows',
    'WindowsInputTypes',
    'CurrentAssembly',
    'CurrentPart',
]

# Global functions for accessing the current Part or Assembly
def CurrentPart() -> Part:
    """Returns a reference to the currently active Part in Alibre Design

    Gets a reference to the Part that is currently open in Alibre Design.
    Does not create a new Part - only returns the existing one.

    Returns:
        Reference to the current Part

    Note:
        Type is Part (not Optional) for coding convenience - no None checking needed.
        Assumes a Part is open when the script runs.

    Example:
        >>> from AlibreScript import *
        >>> MyPart = CurrentPart()
        >>> # No None checking needed - use directly!
        >>> sketch = MyPart.AddSketch('Sketch1', MyPart.XYPlane)
        >>> MyPart.Add3DSketch('3DSketch')
    """
    ...

def CurrentAssembly() -> Assembly:
    """Returns a reference to the currently active Assembly in Alibre Design

    Gets a reference to the Assembly that is currently open in Alibre Design.
    Does not create a new Assembly - only returns the existing one.

    Returns:
        Reference to the current Assembly

    Note:
        Type is Assembly (not Optional) for coding convenience - no None checking needed.
        Assumes an Assembly is open when the script runs.

    Example:
        >>> from AlibreScript import *
        >>> MyAssy = CurrentAssembly()
        >>> # No None checking needed - use directly!
        >>> part = MyAssy.AddPart('Part1', 'C:\\Parts\\MyPart.AD_PRT')
    """
    ...
