"My solution to example 14 in the books numpy section"

import numpy as np

a = np.arange(0,36,1, dtype=int).reshape(6,6)
print(a)

print(a[1,1])
print(a[2,:])
print(a[:,2])
print(a[-1,:])
print(a[:,-1])
print(a[-2,:])
