'My solutions to examples 1 to 4 in the pandas02 module'

import pandas as pd
import numpy as np

# Uppgift 1:
# Skriv en programrad som skapar ett Series-objekt med hjälp av en standard Python lista 
# innehållande udda heltal från 1 till och med 11.

odd_nums = list(range(1,12,2))
sr_odd_nums = pd.Series(odd_nums)

# print(sr_odd_nums)


# Uppgift 2:
# Skriv ett program som konverterar nedanstående strängindexerade fält 'dict_data' 
# till ett Series-objekt med namnet 'ds_data'

dict_data = {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000, 'e': 5000}

ds_data = pd.Series(dict_data)
# print(ds_data)


# Uppgift 3:
# Skriv en programrad som skapar ett Series-objekt med hjälp av en NumPy-array 
# innehållande 6 stycken flyttal mellan 5 och 7.

sr_5_7 = pd.Series(np.linspace(5,7,6))

# print(sr_5_7)


# Uppgift 4:
# Skriv ett program som skapar ett Series-objekt 'ds_heltal' från en standard Python 
# lista 'sp_heltal' innehållande heltalen från 1 t.o.m 6. 
# Index hos 'ds_heltal' ska vara bokstäverna 'a' - 'f'.

sr_int = pd.Series([1, 2, 3, 4, 5, 6])
sr_int.index = ['a', 'b', 'c', 'd', 'e', 'f']

# print(sr_int)
