"My solutions to assignments 7 to 12 in the second set of assignments in the numpy module"

import numpy as np

# 7. Låt  
# A=[[0.,  0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],
#    [1.,  1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9],
#    [2.,  2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9],
#    [3.,  3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9],
#    [4.,  4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9],
#    [5.,  5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9],
#    [6.,  6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 6.9],
#    [7.,  7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7, 7.8, 7.9],
#    [8.,  8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 8.8, 8.9],
#    [9.,  9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 9.9],]
# och därefter extrahera följande element i A genom att använda slicing metoden
# [[0.3 0.7]
#  [4.3 4.7]]

array_7 = np.arange(0,10, 0.1).reshape(10,10)    # better way to create the matrix...

array_7_res = array_7[[0,3],3:8:4]

# print(array_7_res)



# 8. Skapa följande lista: 
# A = [0,4,8, 12, 16, 20, 24,
#  28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72,
#  76, 80, 84, 88, 92, 96]

# och omvandla denna till följande NumPy-array:
# [[ 0  4  8 12 16]
#  [20 24 28 32 36]
#  [40 44 48 52 56]
#  [60 64 68 72 76]
#  [80 84 88 92 96]]
# Extrahera därefter följande element ur Numpy-arrayen 
# [[44 48 52]
#  [64 68 72]]

array_8 = np.arange(0,100,4).reshape(5,5)   #Skipped the create-list-part
# print(array_8[2:4, 1:4])



# 9. Skapa följande två NumPy-arrayer:
# A = [[ 0,  1,  2,  3,  4],
#  [ 5,  6,  7,  8,  9],
#  [10, 11, 12, 13, 14],
#  [15, 16, 17, 18, 19],
#  [20, 21, 22, 23, 24],]

# B = [[20, 21, 22, 23, 24],
#  [25, 26, 27, 28, 29],
#  [30, 31, 32, 33, 34],
#  [35, 36, 37, 38, 39],
#  [40, 41, 42, 43, 44],]
# Skriv därefter ut alla gemensamma element i de två NumPy-arrayerna.

array_9_a = np.arange(0,25).reshape(5,5)
array_9_b = np.arange(20, 45).reshape(5,5)

# print(np.intersect1d(array_9_a, array_9_b))



# 10. Skapa en slumpad NumPy-array med med värden mellan 2 och 15 och följande 
# form och omvandla denna till en vektor (1d NumPy-array).
    
# A = [[12, 11,  2,  6, 12],
#  [ 9, 14, 11, 13, 11],
#  [11, 13,  8, 12, 10],
#  [ 3,  9,  5, 13, 11],
#  [ 3,  9,  7, 10,  9],
#  [ 8,  8,  2,  5, 12],
#  [ 8,  5, 10,  6,  2],
#  [13,  6,  4,  7,  4],
#  [ 6,  2,  5,  9, 10],
#  [10,  5,  3, 10,  2],]

array_10 = np.random.randint(2,16,(10,5))
# print(array_10.flatten())



# 11. Skapa en slumpad NumPy-array med med värden mellan 20 och 135 och följande 
#     form och  och skriv ut maxvärdet i varje rad respektive kolumn.
# A = [[ 46, 125,  36,  88,  62],
#  [ 75,  96,  99, 109,  34],
#  [111,  77, 109,  31,  26],
#  [ 62,  76,  21,  27,  71],
#  [ 47,  93,  35,  21, 130],
#  [ 43, 105,  44,  27,  42],
#  [ 74,  97,  36, 126,  90],
#  [ 55,  51,  52,  65,  79],
#  [ 65,  81,  40, 134, 105],
#  [134,  20,  23,  75, 115],
#  [ 76,  23,  53,  92,  20],
#  [ 72, 110,  81,  90,  98],]

array_11 = np.random.randint(20, 136, (12,5))
# print(array_11)

# for index in range(array_11.shape[0]):
#     print(np.amax(array_11[index, :]))

# for index in range(array_11.shape[1]):
#     print(np.amax(array_11[:,index]))


# 12. Använd Binets formel 
#     fn=[((1+5^1/2)/2)^n-((1-5^1/2)/2)^n]*(1/5^1/2)
#     för att räkna de 15 första talen i Fibonacci talföjlden.

x_12 = np.arange(16)

a_12 = (1+np.sqrt(5))/2
b_12 = (1-np.sqrt(5))/2
c_12 = 1/np.sqrt(5)

array_12 = np.rint((a_12**x_12 - b_12**x_12) * c_12)
array_12 = np.array(array_12, dtype=int)

print(array_12)
