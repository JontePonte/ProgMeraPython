
import numpy as np


a = np.array([
        [1.1, 2.2, 3.3, 4.4],
        [3.1, 4.2, 5.3, 6.4], # I like to always add this comma even thou it's unnecessary
])

b = np.array([
        [1,2,3,4,5,6,7,8],
])

print(a.flatten()*b)