# Auto-import all AlibreScript classes (for VS Code autocomplete only)
from AlibreScript import *

# Template: Get Current Part or Create New
# This template shows the "get or create" pattern - no None checking needed!

# Pattern: Get current part OR create new one if none is open
# The 'or' operator ensures MyPart is never None
MyPart = CurrentPart() or Part('My New Part')

# Now MyPart is guaranteed to be a Part (never None)
# No need for if MyPart check - Pylance knows it's always Part!
print(f"Working with: {MyPart.Name}")

# Add features directly - no type errors!
sketch = MyPart.AddSketch('Profile', MyPart.XYPlane)
sketch.AddCircle(0, 0, 25, False)

MyPart.AddExtrudeBoss('MainBody', sketch, 50, False)

print("Part created or modified successfully!")

# This pattern is perfect when you want to:
# - Modify existing part if one is open
# - Create a new part if nothing is open
# - Never want to show an error message
