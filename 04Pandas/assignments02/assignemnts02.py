
# Övningsuppgifter till Pandas - Datastrukturerna Series- och DataFrame

import pandas as pd

# Uppgift 1:
# Skriv en programrad som skapar ett Series-objekt med hjälp av en standard Python lista 
# innehållande udda heltal från 1 till och med 11.




# Uppgift 2:
# Skriv ett program som konverterar nedanstående strängindexerade fält 'dict_data' 
# till ett Series-objekt med namnet 'ds_data'

dict_data = {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000, 'e': 5000}




# Uppgift 3:
# Skriv en programrad som skapar ett Series-objekt med hjälp av en NumPy-array 
# innehållande 6 stycken flyttal mellan 5 och 7.




# Uppgift 4:
# Skriv ett program som skapar ett Series-objekt 'ds_heltal' från en standard Python 
# lista 'sp_heltal' innehållande heltalen från 1 t.o.m 6. 
# Index hos 'ds_heltal' ska vara bokstäverna 'a' - 'f'.



# Uppgift 5: 
# Skriv en programrad som skapar Series-objektet 'ds_dict' ur en standard Python 
# strängindexerat fält (dict) med innehållet: 
# dict_lista = {'Ett' : 1, 'Två' : 2, 'Tre' : 3, 'Fyra' : 4, 'Fem' : 5}. ds_dict ska vara 
# av datatypen 'float64'




#Uppgift 6:
# Skriv ett program som konverterar nedanstående Series-objekt till en standard Python lista 
# med namnet python_list. 

ds = pd.Series([1, 2, 'tre', 4, 'fem'])




# Uppgift 7:
# Skriv ett program som ändrar nedanstående Series-objekt till float64 genom att 
# 1) använda 'dtype' på Series-objektet ds_1 och 
# 2) använda metoden 'to_numeric' på Series-objektet 'ds_2'. 

# Attributet dtype på ds_1:
ds_1  = pd.Series([1, 2, 3, 4, 5])

# Metoden to_numeric på ds_2:
ds_2  = pd.Series([1, 2, 'tre', 4, 'fem']) 

#Beskriv skillnaden.




# Uppgift 8:
# Skriv ett program som skapar en NumPy-array av nedanstående Series-objekt:

ds = pd.Series([1, 3.3, 4.1, 5.2])




# Uppgift 9:
# Skriv ett program som skapar en standard Python lista med namnet 
# 'python_list' från nedanstående

# DataFrame-objekt:
df = pd.DataFrame([[10, 'tjugo', 30], ['fyrtio', 50, 'sextio']])




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

