# AlibreScript: Basic Sketch Example
# This script demonstrates creating various sketch elements

# Auto-import all AlibreScript classes (for VS Code autocomplete only)
from AlibreScript import *

# Create a new part
MyPart = Part('Sketch Demo')

# Add a sketch
sketch = MyPart.AddSketch('Demo Sketch', MyPart.XYPlane)

# Add a circle (centerX, centerY, radius, isReference)
sketch.AddCircle(0, 0, 10, False)

# Add lines to create a simple shape
sketch.AddLine(20, 0, 40, 0, False)   # Bottom line
sketch.AddLine(40, 0, 40, 20, False)  # Right line
sketch.AddLine(40, 20, 20, 20, False) # Top line
sketch.AddLine(20, 20, 20, 0, False)  # Left line

# Add an arc (centerX, centerY, startX, startY, angle, isReference)
sketch.AddArcCenterStartAngle(60, 10, 60, 0, 90, False)

print 'Sketch created successfully!'
