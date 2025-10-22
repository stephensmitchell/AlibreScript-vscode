"""Auto-generated Python 3 stub file for AlibreScript API

This file provides type hints and documentation for the AlibreScript API.
Compatible with Python 3.6+ and modern IDEs with type checking support.
"""

from typing import Any, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from AlibreScript.Edge import Edge
    from AlibreScript.Vertex import Vertex


class IChamferable:
    """Interface for objects that can have chamfers applied

    Objects that implement this interface (Edge, Vertex) can be used
    as parameters for chamfer operations.
    """

    def ChamferableObject(self) -> Union[Edge, Vertex]:
        """Gets the underlying object that can be chamfered

        Returns:
            The Edge or Vertex object
        """
        ...
