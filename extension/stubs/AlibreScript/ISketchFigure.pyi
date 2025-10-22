"""Auto-generated Python 3 stub file for AlibreScript API

This file provides type hints and documentation for the AlibreScript API.
Compatible with Python 3.6+ and modern IDEs with type checking support.
"""

from typing import Any


class ISketchFigure:
    """Interface for 2D sketch figures (lines, arcs, circles, etc.)

    Objects that implement this interface are sketch entities that can be
    part of a 2D sketch.
    """

    def ToXml(self) -> str:
        """Converts the sketch figure to XML representation

        Returns:
            XML string representing the sketch figure
        """
        ...

    def FigureObject(self) -> Any:
        """Gets the underlying sketch figure object

        Returns:
            The sketch figure object
        """
        ...

    def SetInstance(self, Figure: Any) -> None:
        """Sets the internal figure instance

        Args:
            Figure: The figure instance to set
        """
        ...
