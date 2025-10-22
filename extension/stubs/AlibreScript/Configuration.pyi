"""Auto-generated Python 3 stub file for AlibreScript API

This file provides type hints and documentation for the AlibreScript API.
Compatible with Python 3.6+ and modern IDEs with type checking support.
"""

from typing import Any


class Configuration:

    # Properties (read-only attributes set by Alibre at runtime)
    IsActive: Any  # True if the configuration is currently active
    Name: Any  # The name of the configuration

    def Activate(self) -> None:
        """Makes the configuration active
        """
        ...

    def LockAll(self) -> None:
        """Applies all locks to the configuration
        """
        ...

    def SetLocks(self, Locks: LockTypes) -> None:
        """Sets the locks on the configuration
        
        Args:
            Locks: Locks to set
        """
        ...

    def UnlockAll(self) -> None:
        """Removes all locks from the configuration
        """
        ...
