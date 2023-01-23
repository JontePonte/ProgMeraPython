"Solution of example 5 in the books numpy section"

import numpy as np

a = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])

b = np.tile(a.ravel(), (12,1))  # Tile is nice
print(b)
