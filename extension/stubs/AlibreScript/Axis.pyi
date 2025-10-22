"""Auto-generated Python 3 stub file for AlibreScript API

This file provides type hints and documentation for the AlibreScript API.
Compatible with Python 3.6+ and modern IDEs with type checking support.
"""

from typing import Any


class Axis:

    # Properties (read-only attributes set by Alibre at runtime)
    Name: Any  # The name of the axis

    def GetPart(self) -> Part:
        """Gets the part that the axis is defined on
        
        Returns:
            Part that defines the axis
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
        """Hides the axis
        """
        ...

    def Show(self) -> None:
        """Shows the axis
        """
        ...
