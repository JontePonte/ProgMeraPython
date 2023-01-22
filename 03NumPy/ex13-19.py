"My solution to assignment 13 to 19 in the numpy module"
import numpy as np

#Uppgift 13:
# Skriv en programrad som raderar 1:a och 3:e elementet nedanstående NumPy-array:

array_13 = np.array([1,2,3,4,5,6])
array_13_res = np.delete(array_13, [0,2])

# print(array_13_res)



#Uppgift 14:
# Skriv en programrad som raderar 1:a och 2:a raden i nedanstående NumPy-array:
array_14 = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])

array_14_res = np.delete(array_14, [0,1],0)
# print(array_14_res)


#Uppgift 15:
# Skriv en programrad som raderar 2:a kolumnen i nedanstående NumPy-array:
array_15 = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])

array_15_res = np.delete(array_15, 1,1)
# print(array_15_res)


#Uppgift 16:
# Skriv ett program som reverserar (dvs byter plats på första och sista elementet sist, 
# andra och näst sista elementet osv) för följande np.array:

array_16 =np.array([1,2,3,4,5,6,7,8,9,10])

array_16_res = array_16[::-1]
# print(array_16_res)


#Uppgift 17:
#Skriv ett program som extraherar första kolumnen i nedanstående NumPy-array och lägger resultatet i en ny NumPy-array.

array_17 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]])

array_17_res = array_17[:,0]
# print(array_17_res)


#Uppgift 18:
#Skriv ett program som extraherar andra raden i nedanstående NumPy-array och läggerresultatet i en ny NumPy-array.

array_18 = np.array([[1,2,3],
                          [4,5,6],
                          [7,8,9]])

array_18_res = array_18[1,:]
# print(array_18_res)


#Uppgift 19:
#Skriv ett program som extraherar de två första elementen i första och andra raden i nedanstående NumPy-array och
# lägger resultatet i en ny NumPy-array.

array_19 = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

array_19_res = array_19[[0,1],:2]
print(array_19_res)
