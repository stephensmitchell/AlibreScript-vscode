"""Auto-generated Python 3 stub file for AlibreScript API

This file provides type hints and documentation for the AlibreScript API.
Compatible with Python 3.6+ and modern IDEs with type checking support.
"""

from typing import Any


class Edge:

    # Properties (read-only attributes set by Alibre at runtime)
    Diameter: Any  # The diameter of the edge, if it is a circle
    Length: Any  # The length of the edge
    Name: Any  # Name of the edge

    def GetPart(self) -> Part:
        """Gets the part that the edge is defined on
        
        Returns:
            Part that contains edge
        """
        ...

    def GetSelectionAssembly(self) -> Assembly:
        """The assembly that the edge was selected on
            Only valid when a selection has been made
        
        Returns:
            Assembly or null for no assembly
        """
        ...

    def GetVertices(self) -> List[Vertex]:
        """Gets a python list of the current vertices in the edge
        
        Returns:
            Python list of vertices
        """
        ...
