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
numpy_array = df.to_numpy().astype('int64')

# print(numpy_array)



# Uppgift 11:
# Skapa ett strängindexerat fält (dict) bestående av nycklarna 'Artikelnummer', 'Artikel' 
# och 'Pris' och som innehåller 3 valfria namngivna artiklar 
# med 'Artikelnummer', 'Artikel' och 'Pris'. Konvertera därefter det strängindexerat fältet till 
# ett DataFrame-objekt med namnet 'artikel_data'.

#Solution
data1 = {
    'Article number': [1, 2, 3],
    'Article': ['Fisk', 'Snusktidning', 'Golden Retriever'],
    'Price': [4, 1337, 5]
    }

df_data1 = pd.DataFrame(data1)
df_data1.set_index('Article number', inplace=True)  # Sets article number as index
print(df_data1)

# Messing around. This works as well, perhaps easier as the number and price automatically 
# connects to the article
data2 = [[1, 'Fisk', 4], [2, 'Snusktidning', 1337], [3, 'GolderRetriever', 5]]
df_data2 = pd.DataFrame(data2, columns=['Article number', 'Article', 'Price'])
df_data2.set_index('Article number', inplace=True)
print(df_data2)
