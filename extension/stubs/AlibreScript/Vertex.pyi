"""Auto-generated Python 3 stub file for AlibreScript API

This file provides type hints and documentation for the AlibreScript API.
Compatible with Python 3.6+ and modern IDEs with type checking support.
"""

from typing import Any


class Vertex:

    # Properties (read-only attributes set by Alibre at runtime)
    Name: Any  # Name of the vertex
    X: Any  # X-coordinate of vertex
    Y: Any  # Y-coordinate of vertex
    Z: Any  # Z-coordinate of vertex

    def GetPart(self) -> Part:
        """Part that the vertex is defined on
        
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
