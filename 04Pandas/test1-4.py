"First test file for pandas"

import pandas as pd
import numpy as np

sr_1 = pd.Series([1,2,3,4])
# print(sr_1.values)

sr_2 = pd.Series([1,2,3,4], index=['a', 'b', 'c', 'd'])
# print(sr_2)

dict_3 = {'John': 1337, 'Sofie':'Fin', 'Hugo': 'Barn'}
sr_3 = pd.Series(dict_3)
# print(sr_3.to_numpy())      # Works but gets weird
# print(sr_3)

np_row_n = np.array([1,2,3,4,5,6])
np_row_b = np.array(['bo','bo','bo','bo','bo','stora bo'])

np_data = np.vstack((np_row_n, np_row_b))

df_1 = pd.DataFrame(np_data, index=["siffror", "bo"], columns=['a','b','c','d','e','f'])
df_2 = pd.DataFrame((np_row_n, np_row_b), index=["siffror", "bo"], columns=['a','b','c','d','e','f'])

articles = pd.DataFrame([['1-100', 'Screw', 'M3', '30'],['1-200', 'Screw', 'M4', '30'],\
    ['1-300', 'Screw', 'M5', '50']], columns=['Art. nr', 'Type', 'Size', 'Length'])
articles.set_index('Art. nr', inplace=True)

print(articles)
