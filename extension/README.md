# AlibreScript for VS Code

> **Note:** This extension is in early development. Features and functionality are actively being developed.

Complete AlibreScript development environment with **automatic autocomplete**, type hints, 45+ examples, and interactive notebooks.

## Quick Start - Get Autocomplete in 3 Seconds

1. Create a new Python file
2. Add one line: `from AlibreScript import *`
3. Start coding - full autocomplete for all 47 AlibreScript classes!

```python
# Auto-import all AlibreScript classes (for VS Code autocomplete only)
from AlibreScript import *

# Now get full autocomplete!
MyPart = Part('My Part')  # ← Type 'Part(' and see parameter hints
sketch = MyPart.          # ← Type 'MyPart.' and see all methods
```

**That's it!** One line gives you professional IDE support for AlibreScript.

---

## Features

### IntelliSense & Type Hints
- Full type hints for all AlibreScript API methods
- Parameter documentation on hover
- Autocomplete for classes, methods, and properties
- Type checking with Pylance/Pyright

### Built-in Examples
- 40+ ready-to-use example scripts
- From basic parts to advanced assemblies
- User interface examples
- Import/export demonstrations

### Interactive Notebooks
- Jupyter notebook templates for learning
- Step-by-step tutorials
- Experiment with API calls interactively

### Code Snippets
- Quick snippets for common operations
- Part creation, sketches, features
- User input dialogs
- Assembly constraints

### Commands
- **AlibreScript: New Script from Template** - Create scripts from templates
- **AlibreScript: Open Example** - Browse and open examples
- **AlibreScript: New Interactive Notebook** - Start a new notebook
- **AlibreScript: View API Documentation** - Open official docs

## Getting Started

### Prerequisites
- Visual Studio Code 1.75 or higher (or VS Codium)
- Python extension for VS Code (required)
- Pylance extension (required)
- Python 3.6 or higher installed
- Python Debugger extension (required)
- Jupyter extension (optional, for notebooks)

> **Note:** The extension is designed for Python 3 development. However, AlibreScript runs inside Alibre Design using IronPython 2.7.10. The extension provides modern Python 3 type hints and IntelliSense for development, which enhances the coding experience even though the actual execution environment uses IronPython 2.7.10.

### Quick Start

1. **Create a new script:**
   - Press `Ctrl+Shift+P`
   - Type "AlibreScript: New Script from Template"
   - Choose a template

2. **Use code snippets:**
   - Type `alibre-` and see available snippets
   - Example: `alibre-part` → creates a new part

3. **Get autocomplete:**
   ```python
   MyPart = Part('My Part')
   MyPart.  # <- Autocomplete shows all methods with docs!
   ```

4. **Open examples:**
   - Press `Ctrl+Shift+P`
   - Type "AlibreScript: Open Example"
   - Browse 40+ examples

## Examples Included

- **Basic Operations**
  - Creating parts and sketches
  - Extrusions and cuts
  - Reference geometry

- **Advanced Features**
  - Lofts and sweeps
  - Assemblies and constraints
  - Parameters and configurations

- **User Interface**
  - Input dialogs
  - Option windows
  - Custom forms

- **Data Integration**
  - CSV import
  - Spreadsheet reading
  - File export (STL, STEP, IGES)

## Snippets Reference

| Prefix | Description |
|--------|-------------|
| `alibre-part` | Create a new part |
| `alibre-sketch` | Add a sketch |
| `alibre-circle` | Add a circle |
| `alibre-line` | Add a line |
| `alibre-rectangle` | Add a rectangle |
| `alibre-extrude-boss` | Extrude boss feature |
| `alibre-extrude-cut` | Extrude cut feature |
| `alibre-dialog` | Options dialog |
| `alibre-save` | Save part |
| `alibre-template` | Complete script template |

## Type Hints in Action

The extension provides full type information:

```python
# Autocomplete shows method signature
MyPart.AddExtrudeBoss(
    Name='Boss',      # str
    Sketch=sketch,    # Sketch
    Depth=10.0,       # float
    Flip=False        # bool
)  # Returns: Any

# Hover over methods to see documentation
sketch.AddCircle(...)  # Shows: "Adds a circle to the sketch"
```

## Interactive Notebooks

Start a new notebook to experiment:

1. Command: "AlibreScript: New Interactive Notebook"
2. Choose from:
   - Getting Started
   - Part Creation Tutorial
   - Sketch Tutorial
   - Advanced Features

Notebooks allow you to run code cells individually and see results instantly!

## Configuration

### Settings

- `alibrescript.enableTypeHints` - Enable type hints and autocomplete (default: true)
- `alibrescript.alibrePath` - Path to Alibre Design installation

### Customizing Stubs

The extension includes pre-built type stubs in the `stubs/` directory. These are automatically configured when you open an AlibreScript file.

## API Coverage

Complete stubs for:
- Part operations (extrusions, cuts, lofts, sweeps, etc.)
- Sketch operations (lines, circles, arcs, splines, etc.)
- Assembly operations (constraints, components, etc.)
- Reference geometry (planes, axes, points)
- Parameters and configurations
- User interface (dialogs, forms, input)
- Import/export (STL, STEP, IGES, SAT, etc.)
- Materials and properties

## Troubleshooting

### Autocomplete not working?

1. Make sure Pylance extension is installed
2. Check that Python language mode is active
3. Reload window: `Ctrl+Shift+P` → "Reload Window"

### Type hints not showing?

1. Open settings: `Ctrl+,`
2. Search for "Python Analysis"
3. Set "Type Checking Mode" to "basic" or "standard"

## Contributing

Found a bug or have a suggestion? Please report it on our GitHub repository!

## Resources

- [Official AlibreScript Examples](https://help.alibre.com/articles/#!alibre-help-v28/alibre-script-examples)
- [Alibre Design Website](https://www.alibre.com/)
- [Community Forum](https://www.alibre.com/forum/)

## License

MIT License - See LICENSE file for details

## Disclaimer

This is a community-developed extension and is not officially affiliated with or endorsed by Alibre, Inc.

---

Made for the Alibre community
