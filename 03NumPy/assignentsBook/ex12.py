"Solution to example 12 in the books numpy section"

import numpy as np

a = np.arange(25).reshape(5,5)
print(a)

b = np.sin(a)*3 + 3.0
print(b)
