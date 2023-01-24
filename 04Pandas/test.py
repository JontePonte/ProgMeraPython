"First test file for pandas"

import pandas as pd

sr_1 = pd.Series([1,2,3,4])
# print(sr_1.values)

sr_2 = pd.Series([1,2,3,4], index=['a', 'b', 'c', 'd'])
# print(sr_2)

dict_3 = {'John': 1337, 'Sofie':'Fin', 'Hugo': 'Barn'}
sr_3 = pd.Series(dict_3)
print(sr_3.to_numpy())      # Works but gets weird
