
import numpy as np

# 1. Skriv ett pythonprogram som använder modulen NumPy och generear följande 
# NumPy-array:

list_1 = [[ 0,  1,  2,  3,  4],
    [ 1,  2,  3,  4,  5],
    [ 4,  5,  6,  7,  8],
    [ 9, 10, 11, 12, 13],
    [16, 17, 18, 19, 20]]

array_1 = np.array(list_1)
# print(array_1)

# 2. Skriv ett pythonprogram som använder NumPy-modulen för att 
# generera en talföjld av 20 slumpmässiga tal och omvandlar dessa till
# en matris med 5 rader och 4 kolumner som skrivs ut. Därefter placeras de element 
# i NumPy-arrayen som är större än -0.5 i en ny array och skrivs ut.

array_2 = np.random.random(20)*2 - 1
array_2.resize((5,4))


array_2_res = array_2[array_2>-0.5]
# print(array_2_res)



# 3. Skriv ett pythonprogram som använder modulen NumPy och generear följande 
# NumPy-array och därfter beräknar differensen mellan NumPy-array och dess 
# transponat:

# Vilken typ av NumPy-array(matris) får man som resultat?

list_3=[[0,  1,  2,  3,  4],
        [ 1,  2,  3,  4,  5],
        [ 4,  5,  6,  7,  8],
        [ 9, 10, 11, 12, 13],
        [16, 17, 18, 19, 20]]

array_3 = np.array(list_3)
array_3_trasp = np.transpose(array_3)

array_3_res = array_3 - array_3_trasp

# print(array_3_res)
# Zeros in the diagonal matrix?



# 4. Skapa ett pythonprogram som genererar matrisen
# och skriver ut de element i NumPy-array som är mindre än 5.
list_4 = [[[1, 2, 3],
        [4, 5, 6]],
        [[7, 8, 9],
        [10, 11, 12]]]

array_4 = np.array(list_4)

array_4_res = array_4[array_4 < 5]
# print(array_4_res)


# 5. Skriv ett program som skapar och skriver ut följande matris: 
# A = [[0.,  0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],
#     [1.,  1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9],
#     [2.,  2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9],
#     [3.,  3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9],
#     [4.,  4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9],
#     [5.,  5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9],
#     [6.,  6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 6.9],
#     [7.,  7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7, 7.8, 7.9],
#     [8.,  8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 8.8, 8.9],
#     [9.,  9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 9.9],]

array_5 = np.linspace(0,9.9,100)
array_5.resize(10,10)

# print(array_5)


# 6. Skapa en Pythonprogram som genererar
list_6 = [[[1, 2, 3, 4],
        [5, 6, 7, 8]],
        [[9, 10, 11, 12],
        [13, 14, 15, 16]]]

# och skriver ut elementen
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# genom att använda operatorn %=.§

array_6 = np.array(list_6)

array_6_0100 = np.copy(array_6)
array_6_0100%=2 # Set the elements in the copy matrix to 1 if odd and 2 if even
array_6_mask = np.where(array_6_0100 == 0, True, False) # Create a matrix with the same size where odd numbers = False

array_6_res = array_6[array_6_mask]
# print(array_6_res)
