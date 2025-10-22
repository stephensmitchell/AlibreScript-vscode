"""Auto-generated Python 3 stub file for AlibreScript API

This file provides type hints and documentation for the AlibreScript API.
Compatible with Python 3.6+ and modern IDEs with type checking support.
"""

from typing import Any, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from AlibreScript.Edge import Edge
    from AlibreScript.Face import Face


class IFilletable:
    """Interface for objects that can have fillets applied

    Objects that implement this interface (Edge, Face) can be used
    as parameters for fillet operations.
    """

    def FilletableObject(self) -> Union[Edge, Face]:
        """Gets the underlying object that can be filleted

        Returns:
            The Edge or Face object
        """
        ...
