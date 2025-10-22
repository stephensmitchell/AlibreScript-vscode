"""Auto-generated Python 3 stub file for AlibreScript API

This file provides type hints and documentation for the AlibreScript API.
Compatible with Python 3.6+ and modern IDEs with type checking support.
"""

from typing import Any


class Point:

    # Properties (read-only attributes set by Alibre at runtime)
    Name: Any  # Name of the point
    X: Any  # Point X coordinate
    Y: Any  # Point Y coordinate
    Z: Any  # Point Z coordinate

    def GetCoordinates(self) -> List[float]:
        """Gets the coordiates of the point as a list [X, Y, Z]
        
        Returns:
            List of coordinates [X, Y, Z]
        """
        ...

    def GetPart(self) -> Part:
        """Gets the part that the point is defined in
        """
        ...

    def GetSelectionAssembly(self) -> Assembly:
        """The assembly that the edge was selected on
            Only valid when a selection has been made
        
        Returns:
            Assembly or null for no assembly
        """
        ...

    def Hide(self) -> None:
        """Hides the point
        """
        ...

    def Show(self) -> None:
        """Shows the point
        """
        ...
