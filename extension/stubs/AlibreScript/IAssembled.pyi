"""Auto-generated Python 3 stub file for AlibreScript API

This file provides type hints and documentation for the AlibreScript API.
Compatible with Python 3.6+ and modern IDEs with type checking support.
"""

from typing import Any


class IAssembled:
    """Interface for assembled objects (Parts and SubAssemblies)

    Objects that implement this interface can be assembled into an assembly
    and have occurrences in the assembly structure.
    """

    def GetMappedOccurrence(self, Assembly: Any) -> Any:
        """Gets the occurrence of this object in a specific assembly

        Args:
            Assembly: The assembly to get the occurrence from

        Returns:
            The occurrence object or None if not found
        """
        ...
