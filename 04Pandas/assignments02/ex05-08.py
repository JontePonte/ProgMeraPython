'My solutions to example 5 to 8 in the pandas module 02'

import pandas as pd

# Uppgift 5: 
# Skriv en programrad som skapar Series-objektet 'ds_dict' ur en standard Python 
# strängindexerat fält (dict) med innehållet: 
# dict_lista = {'Ett' : 1, 'Två' : 2, 'Tre' : 3, 'Fyra' : 4, 'Fem' : 5}. ds_dict ska vara 
# av datatypen 'float64'

dict_lista = {'Ett' : 1, 'Två' : 2, 'Tre' : 3, 'Fyra' : 4, 'Fem' : 5}
ds_dict = pd.Series(dict_lista, dtype=float)

# print(ds_dict)



#Uppgift 6:
# Skriv ett program som konverterar nedanstående Series-objekt till en standard Python lista 
# med namnet python_list. 

ds = pd.Series([1, 2, 'tre', 4, 'fem'])
python_list = ds.to_list()  # tolist() also works

print(python_list)


# Uppgift 7:
# Skriv ett program som ändrar nedanstående Series-objekt till float64 genom att 
# 1) använda 'dtype' på Series-objektet ds_1 och 
# 2) använda metoden 'to_numeric' på Series-objektet 'ds_2'. 

# Attributet dtype på ds_1:
ds_1  = pd.Series([1, 2, 3, 4, 5])

# Both of these works fine
ds_1_float = ds_1.astype('float64')
ds_1_float = pd.Series(ds_1, dtype='float64')

# print(ds_1_float)

# Metoden to_numeric på ds_2:
ds_2  = pd.Series([1, 2, 'tre', 4, 'fem'])

ds_2_num = pd.to_numeric(ds_2, downcast='integer', errors='coerce')
# print(ds_2_num)

#Beskriv skillnaden.
# astype and dtype converts numbers to different data types. no_numeric also tries to 
# convert text to numbers


# Uppgift 8:
# Skriv ett program som skapar en NumPy-array av nedanstående Series-objekt:

ds = pd.Series([1, 3.3, 4.1, 5.2])
ds_numpy = ds.to_numpy()

# print(type(ds_numpy))
