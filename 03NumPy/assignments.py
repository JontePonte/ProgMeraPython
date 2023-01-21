

#!/usr/bin/env python
# coding: utf-8


# ***********************************************************************************
# Övningsuppgifter och lösningsförslag till avsnittet NumPy


import numpy as np

# Uppgift 1:
# Skriv en programrad som skapar en endimensionell NumPy-array från nedanstående lista:

lista = [1,2,3,5,7,9]


# Uppgift 2:
# Skapa en NumPy-array med 10 element som innehåller nollor förutom elementet med index = 3 som ska innehålla
# siffran 6.



# Uppgift 3:
# Skapa en NumPy-array som innehåller heltalen från 10 t.o.m 25.



## Uppgift 4:
# Skapa en NumPy-array som innehåller vartannat heltal från -10 t.o.m 10.



# Uppgift 5:
# Skapa en NumPy-array som innehåller vart tredje heltal från -9 t.o.m 12. Typomvandla därefter denna
# NumPy-array till en 'float'.



# Uppgift 6:
# Skapa en NumPy-array som innehåller nedanstående lista i omvänd ordning. 
# [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]



# Uppgift 7:
# Skapa en 2-dimensionell NumPy-array med dimensionen (3,3) där första raden innehåller heltal av ettor (1),
# andra raden heltal av tvåor (2) och tredje raden heltal av treor (3). 
# Typomvandla därefter denna NumPy-array till en 32-bitars flyttal.



#Uppgift 8:
# Visa att man (enkelt) kan skapa en NumPy-array från nedanstående Python tuplett:
a = ([1,2,3], [4,5,6], [7,8,9])



#Uppgift 9:
#Skriv ett program som lägger till element sist i en existerande NumPy-array:
#Ursprunglig array:

np_1 = np.array([1,2,3,4,5])
#Efter att element har lagts till ska NumPy-arrayen ha förljande innehåll:
np_2 = np.array([1,2,3,4,5, 60,70,80])
#Lösning:


#Uppgift 10:
# a. Skriv ett program som skapar en tom NumPy-array som har dimensionen (3,4)
# b. Skriv ett program som skapar en NumPy-array som har dimensionen (3,4) och som innehåller 4:or.



#Uppgift 11:
# Nedanstående lista innehåller temperaturer i Fahrenheit (F). Skriv en programrad som konverterar dessa till
# grader Celsius (C). Formel: C = (5/9*(F-32))

[75, 69, 32, 45, 21]



#Uppgift 12:
# Skriv en programrad som lägger till värdena 100 och 200 fr.o.m. 3:e element nedanstående NumPy-array:

np_1 = np.array([1,2,3,4,5,6])



#Uppgift 13:
# Skriv en programrad som raderar 1:a och 3:e elementet nedanstående NumPy-array:

np_1 = np.array([1,2,3,4,5,6])



#Uppgift 14:
# Skriv en programrad som raderar 1:a och 2:a raden i nedanstående NumPy-array:
np_1 = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])
print(np_2)




#Uppgift 15:
# Skriv en programrad som raderar 2:a kolumnen i nedanstående NumPy-array:
np_1 = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])



#Uppgift 16:
# Skriv ett program som reverserar (dvs byter plats på första och sista elementet sist, 
# andra och näst sista elementet osv) för följande np.array:

np_array =np.array([1,2,3,4,5,6,7,8,9,10])



#Uppgift 17:
#Skriv ett program som extraherar första kolumnen i nedanstående NumPy-array och lägger resultatet i en ny NumPy-array.

numpy_array_1 = np.array([[1,2,3],
                          [4,5,6],
                          [7,8,9]])



#Uppgift 18:
#Skriv ett program som extraherar andra raden i nedanstående NumPy-array och läggerresultatet i en ny NumPy-array.

numpy_array_1 = np.array([[1,2,3],
                          [4,5,6],
                          [7,8,9]])



#Uppgift 19:
#Skriv ett program som extraherar de två första elementen i första och andra raden i nedanstående NumPy-array och
# lägger resultatet i en ny NumPy-array.

A = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])



#Uppgift 20:
#Skriv ett program som extraherar hörnelementen i nedanstående NumPy-array och lägger resultatet i en ny NumPy-array.

A = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])



#Uppgift 21:
#Skriv ett program som extraherar diagonalelementen i nedanstående NumPy-array och lägger resultatet i en ny
#NumPy-array.

A = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])



#Uppgift 22:
# Lägg ihop NumPy-arrayerna A och B genom att skapa en ny Nunpy-array 'C' med dimensionen (3,3) och där
# a. B utgör sista raden i den nya NumPy-array:en 'C'.
# b. B utgör första raden i den nya NumPy-array:en 'C'.

A = np.array([[1,2,3],
              [4,5,6]])
B = np.array([70,80,80])



#Uppgift 23:
# Lägg ihop NumPy-arrayerna A och B genom att skapa en ny Nunpy-array 'C' med dimensionen (2,4) och där
# a. B utgör sista kolumnen i den nya NumPy-array:en 'C'.
# b. B utgör första kolumnen i den nya NumPy-array:en 'C'.

A = np.array([[1,2,3],
              [4,5,6]])
B = np.array([70,80,80])
