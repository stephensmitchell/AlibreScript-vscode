"""Auto-generated Python 3 stub file for AlibreScript API

This file provides type hints and documentation for the AlibreScript API.
Compatible with Python 3.6+ and modern IDEs with type checking support.
"""

from typing import Any


class IConstrainable:
    """Interface for objects that can be constrained in assemblies

    Objects that implement this interface can be used as constraint references
    in assembly constraints.
    """

    def ConstraintObject(self) -> Any:
        """Gets the underlying constraint object

        Returns:
            The constraint object
        """
        ...
