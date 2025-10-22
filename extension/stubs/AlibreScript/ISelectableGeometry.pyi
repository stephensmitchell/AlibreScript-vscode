"""Auto-generated Python 3 stub file for AlibreScript API

This file provides type hints and documentation for the AlibreScript API.
Compatible with Python 3.6+ and modern IDEs with type checking support.
"""

from typing import Any


class ISelectableGeometry:
    """Interface for geometry that can be selected

    Objects that implement this interface can be used in selection operations
    and as references for constraints and features.
    """

    def SelectableObject(self) -> Any:
        """Gets the underlying selectable geometry object

        Returns:
            The geometry object
        """
        ...
