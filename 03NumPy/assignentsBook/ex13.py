"My solution to example 13 in the books numpy section"

import numpy as np

a = np.random.randint(0,100,(5,5))
b = np.random.randint(0,100,(5,5))

# Three ways of doing matrix multiplication
c = np.dot(a,b)
print(c)

d = a @ b
print(d)

e = np.matrix(a)
f = np.matrix(b)
g = e*f
print(g)
