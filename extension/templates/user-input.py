# AlibreScript: User Input Example
# This script demonstrates getting user input and using it to create a part

# Auto-import all AlibreScript classes (for VS Code autocomplete only)
from AlibreScript import *

# Get dimensions from user
print 'Enter width (mm):'
width = float(Read())

print 'Enter height (mm):'
height = float(Read())

print 'Enter depth (mm):'
depth = float(Read())

# Validate input
if width <= 0 or height <= 0 or depth <= 0:
    raise ValueError('All dimensions must be greater than 0')

# Create the part
print 'Creating part with dimensions: %f x %f x %f mm' % (width, height, depth)

MyPart = Part('Custom Box')
sketch = MyPart.AddSketch('Profile', MyPart.XYPlane)
sketch.AddRectangle(0, 0, width, height, False)
MyPart.AddExtrudeBoss('Box', sketch, depth, False)

print 'Part created successfully!'
