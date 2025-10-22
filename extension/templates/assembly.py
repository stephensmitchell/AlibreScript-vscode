# AlibreScript: Assembly Creation
# This script creates a simple assembly

# Auto-import all AlibreScript classes (for VS Code autocomplete only)
from AlibreScript import *

# Create a new assembly
MyAssembly = Assembly('Basic Assembly')

# Optional: Insert components
# MyAssembly.InsertNewPart('Part1')
# MyAssembly.InsertExistingPart('C:\\Path\\To\\Part.AD_PRT')

print 'Assembly created successfully!'
