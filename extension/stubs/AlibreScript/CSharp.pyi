"""Auto-generated Python 3 stub file for AlibreScript API

This file provides type hints and documentation for the AlibreScript API.
Compatible with Python 3.6+ and modern IDEs with type checking support.
"""

from typing import Any
from typing import overload


class CSharp:

    def Compile(self, Code: str) -> bool:
        """Compiles C# code
        
        Args:
            Code: Code to compile
        
        Returns:
            Compiled code object
        """
        ...

    @overload
    def CompileAndRun(self, Code: str) -> bool:
        """Compiles and runs C# code
        
        Args:
            Code: Code to compile and run
        
        Returns:
            Updated dictionary of variables
        """
        ...

    @overload
    def CompileAndRun(self, Code: str, Variables: PythonDictionary) -> bool:
        """Compiles and runs C# code
        
        Args:
            Code: Code to compile and run
            Variables: Dictionary of variables
        
        Returns:
            Updated dictionary of variables
        """
        ...

    @overload
    def Run(self, Script: Any) -> Any:
        """Runs compiled C# code
        
        Args:
            Script: Compiled code object to run
        
        Returns:
            Updated dictionary of variables
        """
        ...

    @overload
    def Run(self, Script: Any, Variables: PythonDictionary) -> Any:
        """Runs compiled C# code
        
        Args:
            Script: Compiled code object to run
            Variables: Dictionary of variables or None for no variables
        
        Returns:
            Updated dictionary of variables
        """
        ...
