"""Auto-generated Python 3 stub file for AlibreScript API

This file provides type hints and documentation for the AlibreScript API.
Compatible with Python 3.6+ and modern IDEs with type checking support.
"""

from typing import Any, List
from typing import overload


class Windows:

    def CloseForm(self, SessionIdentifier: str) -> None:
        """Close all currently open forms for a specific session
        
        Args:
            SessionIdentifier: Identifier for session
        """
        ...

    def DisableInput(self, Index: int) -> None:
        """Disables an input
        
        Args:
            Index: Index of the input
        """
        ...

    def EnableInput(self, Index: int) -> None:
        """Enables an input
        
        Args:
            Index: Index of the input
        """
        ...

    def ErrorDialog(self, Message: str, Title: str) -> None:
        """Shows an error window
        
        Args:
            Message: Error message
            Title: Title of window
        """
        ...

    def GetDisplayedForm(self, SessionIdentifier: str) -> str:
        """Gets the currently displayed form for a specific session
        
        Args:
            SessionIdentifier: Identifier of session
        
        Returns:
            Displayed form or null for none
        """
        ...

    def GetInputValue(self, Index: int) -> str:
        """Gets the current value of an input
        
        Args:
            Index: Index of the input
        
        Returns:
            Current value
        """
        ...

    def InfoDialog(self, Message: str, Title: str) -> None:
        """Shows an information window
        
        Args:
            Message: Message to show
            Title: Title of window
        """
        ...

    def OpenFileDialog(self, Title: str = "Open File", Filter: str = "All Files|*.*", DefaultExtension: str = "") -> str:
        """Prompts user to select a file

        Args:
            Title: Title of dialog window (default: "Open File")
            Filter: File filter, example filter: 'Part Files|*.AD_PRT' (default: "All Files|*.*")
            DefaultExtension: Default file extension, e.g. '.AD_PRT' (default: "")

        Returns:
            Path and name of selected file or empty string if canceled
        """
        ...

    @overload
    def OptionsDialog(self, Title: str, Inputs: List[List[Any]], InputAreaWidth: int = 400) -> int:
        """Shows a dialog prompting the user to enter values

        Args:
            Title: Title of dialog window
            Inputs: List of input definitions [[Name, Type, DefaultValue], [...]]
            InputAreaWidth: Width of input area (default: 400)

        Returns:
            List of entered values
        """
        ...

    @overload
    def OptionsDialog(self, Title: str, Inputs: List[List[Any]], InputAreaWidth: int, InputChangedCallback: Any, UpdateUserInterfaceCallback: Any) -> int:
        """Shows a dialog prompting the user to enter values

        Args:
            Title: Title of dialog window
            Inputs: List of input definitions
            [[Name, Type, DefaultValue, OptionalSettings], [...]]
            Example: ['Image', WindowsInputTypes.Image, 'Logo.png']
            InputAreaWidth: Width of input area
            InputChangedCallback: Function called when an input is changed
            UpdateUserInterfaceCallback: Function called after dialog is created to update the state of the dialog

        Returns:
            List of entered values
        """
        ...

    def QuestionDialog(self, Question: str, Title: str) -> int:
        """Shows a question window
        
        Args:
            Question: Question to show
            Title: Title of window
        
        Returns:
            true if 'yes' was clicked, false if 'no' was clicked
        """
        ...

    def SaveFileDialog(self, Title: str = "Save File", Filter: str = "All Files|*.*", DefaultExtension: str = "") -> str:
        """Prompts user to save a file

        Args:
            Title: Title of dialog window (default: "Save File")
            Filter: File filter, example filter: 'Part Files|*.AD_PRT' (default: "All Files|*.*")
            DefaultExtension: Default file extension, e.g. '.AD_PRT' (default: "")

        Returns:
            Path and name of selected file or empty string if canceled
        """
        ...

    def SelectFolderDialog(self, CurrentFolder: str = "", Description: str = "Select Folder") -> str:
        """Prompts the user to select a folder

        Args:
            CurrentFolder: The current folder, if any (default: "")
            Description: Description of what is being chosen, shown to user (default: "Select Folder")

        Returns:
            Path of selected folder or empty if canceled
        """
        ...

    def SetInputValue(self, Index: int, Value: Any) -> None:
        """Sets the current value for an input
        
        Args:
            Index: Index of the input
            Value: Value to show
        """
        ...

    def SetStringList(self, Index: int, Strings: Any) -> None:
        """Updates the list of strings for a stringlist input
        
        Args:
            Index: Index of the stringlist input
            Strings: New list of strings to show
        """
        ...

    @overload
    def UtilityDialog(self, Title: str, ActionButtonText: str, ActionButtonCallback: Any, InputChangedCallback: Any, Inputs: List[List[Any]], InputAreaWidth: int = 400) -> int:
        """Shows a dialog prompting the user to enter values
            The dialog remains open until the user clicks on the close button
            A callback function is called to give the input values to the script

        Args:
            Title: Title of dialog window
            ActionButtonText: Text for action button
            ActionButtonCallback: Function called when the action button is clicked
            InputChangedCallback: Function called when an input is changed
            Inputs: List of input definitions [[Name, Type, DefaultValue, OptionalSettings], [...]]
            InputAreaWidth: Width of dialog input area (default: 400)
        """
        ...

    @overload
    def UtilityDialog(self, Title: str, ActionButtonText: str, ActionButtonCallback: Any, InputChangedCallback: Any, Inputs: List[List[Any]], InputAreaWidth: int, UpdateUserInterfaceCallback: Any) -> int:
        """Shows a dialog prompting the user to enter values
            The dialog remains open until the user clicks on the close button
            A callback function is called to give the input values to the script

        Args:
            Title: Title of dialog window
            ActionButtonText: Text for action button
            ActionButtonCallback: Function called when the action button is clicked
            InputChangedCallback: Function called when an input is changed
            Inputs: List of input definitions
            [[Name, Type, DefaultValue, OptionalSettings], [...]]
            Example: ['Image', WindowsInputTypes.Image, 'Logo.png']
            InputAreaWidth: Width of dialog input area
            UpdateUserInterfaceCallback: Function called after dialog is created to update the state of the dialog
        """
        ...
