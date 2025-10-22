"""Auto-generated Python 3 stub file for AlibreScript API

This file provides type hints and documentation for the AlibreScript API.
Compatible with Python 3.6+ and modern IDEs with type checking support.
"""

from typing import Any


class Parameter:

    # Properties (read-only attributes set by Alibre at runtime)
    Comment: Any  # Comment for the parameter
    Equation: Any  # Equation of the parameter
    ExcelCell: Any  # Excel cell associated with the parameter, e.g. '$B$3'
    ExcelSheet: Any  # Excel sheet associated with the parameter, e.g. 'Sheet1'
    ExcelWorkbook: Any  # Excel workbook associated with the parameter e.g. 'Foo.xlsx'
    Name: Any  # Name of the parameter
    RawValue: Any  # Raw value of the parameter
    Type: Any  # Type of the parameter
    Units: Any  # Current units of the parameter
    Value: Any  # Current value of the parameter in script units (for mm, cm, in), or degrees for angles, or raw value for other units

    def AttachToExcel(self, Document: str, Sheet: str, Cell: str, Units: UnitTypes) -> None:
        """Attaches the parameter to a cell in an Ezcel spreadsheet
        
        Args:
            Document: Path and name of Excel spreadsheet
            Sheet: Name of sheet to use
            Cell: Cell to use
            Units: Units used in the cell
        """
        ...
