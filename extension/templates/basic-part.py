# AlibreScript: Basic Part Creation
# This script creates a simple rectangular part

# Auto-import all AlibreScript classes (for VS Code autocomplete only)
from AlibreScript import *

# Create a new part
MyPart = Part('Basic Part')

# Add a sketch on the XY plane
sketch = MyPart.AddSketch('Profile', MyPart.XYPlane)

# Draw a rectangle (x, y, width, height, isReference)
sketch.AddRectangle(0, 0, 50, 30, False)

# Extrude the sketch (name, sketch, depth, flip)
MyPart.AddExtrudeBoss('Main Body', sketch, 10, False)

# Optional: Save the part
# MyPart.Save('C:\\Path\\To\\Folder')

print 'Part created successfully!'
