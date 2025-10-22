"""Auto-generated Python 3 stub file for AlibreScript API

This file provides type hints and documentation for the AlibreScript API.
Compatible with Python 3.6+ and modern IDEs with type checking support.
"""

from typing import Any, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from AlibreScript.Plane import Plane
    from AlibreScript.Face import Face


class ISketchSurface:
    """Interface for sketch surfaces (Plane or Face)

    A sketch surface can be either a Plane or a Face that a sketch can be drawn on.
    This interface is used as a parameter type for methods that accept either type.
    """

    def SurfaceObject(self) -> Union[Plane, Face]:
        """Gets the underlying surface object

        Returns:
            The Plane or Face object
        """
        ...
