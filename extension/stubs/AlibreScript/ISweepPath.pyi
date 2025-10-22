"""Auto-generated Python 3 stub file for AlibreScript API

This file provides type hints and documentation for the AlibreScript API.
Compatible with Python 3.6+ and modern IDEs with type checking support.
"""

from typing import Any, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from AlibreScript.Sketch import Sketch
    from AlibreScript.Sketch3D import Sketch3D
    from AlibreScript.Edge import Edge


class ISweepPath:
    """Interface for sweep paths (Sketch, Sketch3D, or Edge)

    A sweep path defines the trajectory along which a profile is swept.
    This interface is used as a parameter type for methods that accept path objects.
    """

    def PathObject(self) -> Union[Sketch, Sketch3D, Edge]:
        """Gets the underlying path object

        Returns:
            The Sketch, Sketch3D, or Edge object used as the path
        """
        ...
