"""Auto-generated Python 3 stub file for AlibreScript API

This file provides type hints and documentation for the AlibreScript API.
Compatible with Python 3.6+ and modern IDEs with type checking support.
"""

from typing import Any


class AssembledSubAssembly:

    # Properties (read-only attributes set by Alibre at runtime)
    Configurations: Any  # A list of configurations defined on the assembly
    Name: Any  # Name of the subassembly

    def GetConfiguration(self, Name: str) -> Configuration:
        """Gets a configuration with a specific name
        
        Args:
            Name: Name of confguration
        
        Returns:
            Configuration object
        """
        ...

    def GetMappedOccurrence(self, Assembly: IADAssemblySession) -> Any:
        """Gets the occurrence of the sub-assembly mapped into the 
            occurrence structure of a specific assembly
            This occurrence can be used to create constraints in the specific
            sub-assembly using the part
        
        Args:
            Assembly: Assembly for occurrence structure
        
        Returns:
            Mapped occurrence or null if not found
        """
        ...

    def GetSelectionAssembly(self) -> Assembly:
        """The assembly that the edge was selected on
            Only valid when a selection has been made
        
        Returns:
            Assembly or null for no assembly
        """
        ...
