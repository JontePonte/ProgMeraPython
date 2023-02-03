'My solutions to exmples 9 to 11 in the pandas module 02'

import pandas as pd

# Uppgift 9:
# Skriv ett program som skapar en standard Python lista med namnet 
# 'python_list' från nedanstående

# DataFrame-objekt:
df = pd.DataFrame([[10, 'tjugo', 30], ['fyrtio', 50, 'sextio']])

df_list = df.values.tolist() # a bit weird but to_list() does not work...
# print(df_list)


# Uppgift 10:
# Skriv ett program som skapar en NumPy-array med namnet 'numpy_array' 
# från nedanstående DataFrame-objekt. 

# Numpy-arrayen ska vara av typen 'int64'
df = pd.DataFrame([[10.3, 9.9, 30.0], [14.3, -50.6, 17.9]])




# Uppgift 11:
# Skapa ett strängindexerat fält (dict) bestående av nycklarna 'Artikelnummer', 'Artikel' 
# och 'Pris' och som innehåller 3 valfria namngivna artiklar 
# med 'Artikelnummer', 'Artikel' och 'Pris'. Konvertera därefter det strängindexerat fältet till 
# ett DataFrame-objekt med namnet 'artikel_data'.

