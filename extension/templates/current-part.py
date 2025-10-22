# Auto-import all AlibreScript classes (for VS Code autocomplete only)
from AlibreScript import *

# Template: Working with Currently Open Part
# This template shows how to safely use CurrentPart() with proper type checking

# Get the currently open part
MyPart = CurrentPart()

# IMPORTANT: Always check if MyPart is None before using it!
if MyPart:
    # Safe to use - Pylance knows MyPart is Part, not None
    print(f"Working with part: {MyPart.Name}")

    # Add a sketch
    sketch = MyPart.AddSketch('NewSketch', MyPart.XYPlane)
    sketch.AddRectangle(0, 0, 50, 30, False)

    # Add a feature
    MyPart.AddExtrudeBoss('NewBoss', sketch, 10, False)

    # Add a 3D sketch
    sketch3d = MyPart.Add3DSketch('3DSketch')

    print("Features added successfully!")
else:
    # No part is currently open
    print("ERROR: No part is currently open!")
    print("Please open a part in Alibre Design before running this script.")
