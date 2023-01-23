"Solution for example 4 in the book"

import numpy as np

a = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])

print(a)
print(a.reshape(-1))    # reshape(1,12) creates a 2-dim array [[1,2,3,4...]]
print(a.ravel())        # just like reshape(-1)
print(a.flatten())      # like the previous two but returns a copy
