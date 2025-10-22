"""Auto-generated Python 3 stub file for AlibreScript API

This file provides type hints and documentation for the AlibreScript API.
Compatible with Python 3.6+ and modern IDEs with type checking support.
"""

from typing import Any


class Face:

    # Properties (read-only attributes set by Alibre at runtime)
    Name: Any  # The name of the face

    def DistanceTo(self, OtherFace: Face) -> float:
        """Gets the distance from this face to another face
        
        Args:
            OtherFace: The other face to measure to
        
        Returns:
            The distance between faces
        """
        ...

    def GetAdjoiningFaces(self) -> List[Face]:
        """Gets a list of the adjoining faces
        
        Returns:
            List of faces
        """
        ...

    def GetArea(self) -> float:
        """Gets the area of the face
        
        Returns:
            Area of face
        """
        ...

    def GetEdges(self) -> List[Edge]:
        """Gets a list of the current edges in the face
        
        Returns:
            List of edges
        """
        ...

    def GetPart(self) -> Part:
        """Gets the part that the face is defined on
        
        Returns:
            Part that contains face
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
        """Gets a list of the current vertices in the face
        
        Returns:
            List of vertices
        """
        ...

    def IsParallel(self, OtherFace: Face) -> bool:
        """Checks if another face is parallel to this one
        
        Args:
            OtherFace: The other face to check
        
        Returns:
            true if the faces are parallel
        """
        ...

    def IsRectangle(self) -> bool:
        """Determines if the face is a rectangle
        
        Returns:
            true if face is a rectangle
        """
        ...
