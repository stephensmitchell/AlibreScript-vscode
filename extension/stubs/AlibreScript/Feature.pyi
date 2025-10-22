"""Auto-generated Python 3 stub file for AlibreScript API

This file provides type hints and documentation for the AlibreScript API.
Compatible with Python 3.6+ and modern IDEs with type checking support.
"""

from typing import Any


class Feature:

    # Properties (read-only attributes set by Alibre at runtime)
    Name: Any  # Name of the feature

    def SetColor(self, Red: int, Green: int, Blue: int) -> None:
        """Sets the color of the part
        
        Args:
            Red: Red component 0 - 255
            Green: Green component 0 - 255
            Blue: Blue component 0 - 255
        """
        ...
