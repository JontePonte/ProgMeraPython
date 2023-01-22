"My solutions to assignment 20 to 23 in the numpy module"

import numpy as np

#Uppgift 20:
#Skriv ett program som extraherar hörnelementen i nedanstående NumPy-array och lägger resultatet i en ny NumPy-array.

array_20 = np.array([[1,2,3,4],
              [4,5,6,7],
              [4,5,6,7],
              [4,5,6,7],
              [7,8,9,10]])

x, y = array_20.shape   # Fancy, universal way of doing it
array_20_res = array_20[::x-1,::y-1]
# print(array_20_res)


#Uppgift 21:
#Skriv ett program som extraherar diagonalelementen i nedanstående NumPy-array och lägger resultatet i en ny
#NumPy-array.

array_21 = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

array_20_res = array_21[[0,1,2],[0,1,2]]
# print(array_20_res)


#Uppgift 22:
# Lägg ihop NumPy-arrayerna A och B genom att skapa en ny Nunpy-array 'C' med dimensionen (3,3) och där
# a. B utgör sista raden i den nya NumPy-array:en 'C'.
# b. B utgör första raden i den nya NumPy-array:en 'C'.

array_22_a = np.array([[1,2,3],
                      [4,5,6]])

array_22_b = np.array([70,80,80])

array_22_res_a = np.vstack((array_22_a, array_22_b))
array_22_res_b = np.vstack((array_22_b, array_22_a))

# print(array_22_res_a)
# print(array_22_res_b)


#Uppgift 23:
# Lägg ihop NumPy-arrayerna A och B genom att skapa en ny Nunpy-array 'C' med dimensionen (2,4) och där
# a. B utgör sista kolumnen i den nya NumPy-array:en 'C'.
# b. B utgör första kolumnen i den nya NumPy-array:en 'C'.

array_23_a = np.array([[1,2,3],
                        [4,5,6]])
array_23_b = np.array([70,80,80])

new_2_1 = array_23_b[:2]
new_2_1.resize(2,1)

array_23_res_a = np.hstack((array_23_a, new_2_1))
array_23_res_b = np.hstack((new_2_1, array_23_a))

print(array_23_res_a)
print(array_23_res_b)
