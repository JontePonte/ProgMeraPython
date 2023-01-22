"My solutions to examples 1 to 5 in the numpy module"
import numpy as np

# Uppgift 1:
# Skriv en programrad som skapar en endimensionell NumPy-array från nedanstående lista:

list_1 = [1,2,3,5,7,9]
array_1 = np.array(list_1)
# print(type(array_1))


# Uppgift 2:
# Skapa en NumPy-array med 10 element som innehåller nollor förutom elementet med 
# index = 3 som ska innehålla siffran 6.

array_2 = np.zeros(10)
array_2[3] = 6
# print(array_2)


# Uppgift 3:
# Skapa en NumPy-array som innehåller heltalen från 10 t.o.m 25.

array_3 = np.linspace(10,25,16)
# print(array_3)


## Uppgift 4:
# Skapa en NumPy-array som innehåller vartannat heltal från -10 t.o.m 10.

array_4 = np.linspace(-10,10,21)
# print(array_4)


# Uppgift 5:
# Skapa en NumPy-array som innehåller vart tredje heltal från -9 t.o.m 12. Typomvandla därefter denna
# NumPy-array till en 'float'.

array_5_int = np.arange(-9,13,3)
array_5_float = array_5_int.astype(float)

print(array_5_int)
print(array_5_float)
