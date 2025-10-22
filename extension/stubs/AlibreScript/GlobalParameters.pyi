"""Auto-generated Python 3 stub file for AlibreScript API

This file provides type hints and documentation for the AlibreScript API.
Compatible with Python 3.6+ and modern IDEs with type checking support.
"""

from typing import Any
from typing import overload


if TYPE_CHECKING:
    from AlibreScript.Configuration import Configuration
    from AlibreScript.Parameter import Parameter


class GlobalParameters:


    @overload
    def __init__(self, folder: str, name: str) -> None:
        """Opens an existing global parameters set

        Args:
            folder: Folder containing global parameters
            name: Name of global parameters to open
        """
        ...

    @overload
    def __init__(self, name: str) -> None:
        """Creates a new global parameters set

        Args:
            name: Name of new global parameters set
        """
        ...

    @overload
    def __init__(self, name: str, create_new: bool) -> None:
        """Creates a new global parameters set or accesses an already opened global parameters set

        Args:
            name: Name of global parameters set to create or access
            create_new: True to create a new global parameters set, false to access an opened one
        """
        ...

    # Properties (read-only attributes set by Alibre at runtime)
    Configurations: Any  # A list of configurations
    Name: Any  # Name of the global parameters
    Parameters: Any  # A list of parameters

    @overload
    def AddConfiguration(self, Name: str) -> Configuration:
        """Adds a configuration to the global parameters set
        
        Args:
            Name: Name of configuration
        
        Returns:
            New configuration
        """
        ...

    @overload
    def AddConfiguration(self, Name: str, BaseConfigurationName: str) -> Configuration:
        """Adds a configuration to the global parameters set using another configuration as a base
        
        Args:
            Name: Name of configuration
            BaseConfigurationName: Name of base configuration to use
        
        Returns:
            New configuration
        """
        ...

    @overload
    def AddParameter(self, Name: str, Type: ParameterTypes, Value: float) -> Parameter:
        """Adds a parameter to the global parameters set
        
        Args:
            Name: Name of parameter
            Type: Type of parameter
            Value: Value for parameter
        
        Returns:
            New parameter
        """
        ...

    @overload
    def AddParameter(self, Name: str, Type: ParameterTypes, Equation: str) -> Parameter:
        """Adds a parameter to the global parameters set
        
        Args:
            Name: Name of parameter
            Type: Type of parameter
            Equation: Equation for parameter
        
        Returns:
            New parameter
        """
        ...

    def Close(self) -> None:
        """Closes the global parameters set
            If it is unsaved then changes will be lost
        """
        ...

    def GetActiveConfiguration(self) -> Any:
        """Gets the currently active configuration
        
        Returns:
            Configuration object
        """
        ...

    def GetConfiguration(self, Name: str) -> Configuration:
        """Gets a configuration with a specific name
        
        Args:
            Name: Name of confguration
        
        Returns:
            Configuration object
        """
        ...

    def GetParameter(self, Name: str) -> Parameter:
        """Gets a parameter with a specific name
        
        Args:
            Name: Name of parameter
        
        Returns:
            Parameter object
        """
        ...

    @overload
    def Save(self) -> None:
        """Saves the global parameters set using the current path and file name
        """
        ...

    @overload
    def Save(self, Folder: str) -> None:
        """Saves the global parameters set to a specific folder
        
        Args:
            Folder: Folder to save to
        """
        ...

    def SaveAs(self, Folder: str, NewName: str) -> None:
        """Saves the global parameters set to a specific folder with a new name
        
        Args:
            Folder: Folder to save to
            NewName: New name for global parameters set
        """
        ...
