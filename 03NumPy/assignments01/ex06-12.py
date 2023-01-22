"My solutions to assignment 6-10 in the numpy module"

import numpy as np

# Uppgift 6:
# Skapa en NumPy-array som innehåller nedanstående lista i omvänd ordning. 
# [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

array_6 = np.array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])

array_6_backwards = array_6[-1::-1]
# print(array_6_backwards)



# Uppgift 7:
# Skapa en 2-dimensionell NumPy-array med dimensionen (3,3) där första raden innehåller heltal av ettor (1),
# andra raden heltal av tvåor (2) och tredje raden heltal av treor (3). 
# Typomvandla därefter denna NumPy-array till en 32-bitars flyttal.

matrix_7_int = np.array([
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3],
])

matrix_7_float32 = np.array(matrix_7_int, dtype='float32')
# print(matrix_7_float32)
# print(type(matrix_7_float32[1,1]))


#Uppgift 8:
# Visa att man (enkelt) kan skapa en NumPy-array från nedanstående Python tuplett:
tupl_8 = ([1,2,3], [4,5,6], [7,8,9])

matrix_8 = np.array(tupl_8)
# print(matrix_8)


#Uppgift 9:
#Skriv ett program som lägger till element sist i en existerande NumPy-array:
#Ursprunglig array:

array_9 = np.array([1,2,3,4,5])
#Efter att element har lagts till ska NumPy-arrayen ha förljande innehåll:
# np_2 = np.array([1,2,3,4,5, 60,70,80])

array_9_extra = np.array([60,70,80])

array_9_result = np.hstack((array_9, array_9_extra))
# print(array_9_result)

# Uppgift 10:
# a. Skriv ett program som skapar en tom NumPy-array som har dimensionen (3,4)
# b. Skriv ett program som skapar en NumPy-array som har dimensionen (3,4) och som innehåller 4:or.

array_10_a = np.ones((3,4))
array_10_b = array_10_a*4

# print(array_10_a)
# print(array_10_b)


#Uppgift 11:
# Nedanstående lista innehåller temperaturer i Fahrenheit (F). Skriv en programrad som konverterar dessa till
# grader Celsius (C). Formel: C = (5/9*(F-32))

temps_F = np.array([75, 69, 32, 45, 21])
temps_C = 5/9*(temps_F-32)

# print(temps_F)
# print(temps_C)

#Uppgift 12:
# Skriv en programrad som lägger till värdena 100 och 200 fr.o.m. 3:e element nedanstående NumPy-array:

np_12 = np.array([1,2,3,4,5,6])

np_12_res = np.hstack((np_12[:3]+100, np_12[3:]+200))

print(np_12_res)

