"My solutions to assignments 13 to 17 in the second assignment list in the numpy module"

import numpy as np

# 13. Skriv en program som skapar nedanstående Numpy-array 
#     och därfter använder Numpys inbyggda funktioner add(), multiply(), subtract() 
# och divide() för att beräkna 
#     summan, produkten, skillnaden och kvoten av A och B.
# A = [[ 1,  2,  3,  4],
#  [ 5,  6,  7,  8],
#  [ 9, 10, 11, 12],
#  [13, 14, 15, 16],]

# B = [[11, 12, 13, 14],
#  [15, 16, 17, 18],
#  [19, 20, 21, 22],
#  [23, 24, 25, 26],]

array_13_a = np.arange(1,17).reshape(4,4)
array_13_b = np.arange(11,27).reshape(4,4)

# print(np.add(array_13_a, array_13_b))
# print(np.multiply(array_13_a, array_13_b))
# print(np.subtract(array_13_a, array_13_b))
# print(np.divide(array_13_a, array_13_b))


# 14. Använda Numpy funktion where() för att omvandla följande Numpy-array:
# A = [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9],]

# till Numpy-arrayen:
# [[ 1  2  3]
#  [ 4  5 12]
#  [12 12 12]]

array_14 = np.arange(1,10,1)
array_14 = np.where(array_14 >=6, 12, array_14)

# print(array_14)

# 15. Man kan använda  funktionen array_split() för dela en Numpy-array till olika 
# sub Numpy-arrayer. 
# Använd denna funktion för att skapa 5 sub Numpy-array från:
# A = [[ 1,  2,  3,  4,  5,  6,  7],
#  [ 8,  9, 10, 11, 12, 13, 14],
#  [15, 16, 17, 18, 19, 20, 21],
#  [22, 23, 24, 25, 26, 27, 28],
#  [29, 30, 31, 32, 33, 34, 35],
#  [36, 37, 38, 39, 40, 41, 42],
#  [43, 44, 45, 46, 47, 48, 49],]

array_15 = np.arange(1,50).reshape(7,7)

# print(np.array_split(array_15,5))


# 16. Skapa följande Numpy-array
# A=[ 6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 11, 11, 11, 11, 11]
# genom att använda funktionen where() från Nympy-arrayen:
# B=[ 6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26] 

# och därfter hitta positionen för talet 11 i A med hjälp av samma funktion. 

array_16 = np.arange(6,27,1)

array_16_res = np.where(array_16 > 20, 11, array_16)
# print(array_16_res == 11, True, False))



# 17. Använda  sort() funktionen för att sortera Numpy-array:
#     ['Röd', 'Grön', 'Vitt', 'Svart','Lilla','Gull', 'violet','Mörkröd','Blå']
#     och skriv därefter ut positionen för 'Svart' före och efter sorteringen.

array_17 = np.array(['Röd', 'Grön', 'Vitt', 'Svart','Lilla','Gull', 'violet','Mörkröd','Blå'])
array_17_sort = np.sort(array_17)

# print(np.argwhere(array_17 == 'Svart'))
# print(np.argwhere(array_17_sort == 'Svart'))


# 18. Skriv ett program som använder funktionerna lcm() och gcd() för att beräkna
#     minsta gemensamma multipel och största gemensamma nämnare av två tal som du 
# matar in.

num_18_a = int(input("Nr 1: "))
num_18_b = int(input("Nr 2: "))

print(np.lcm(num_18_a, num_18_b))
print(np.gcd(num_18_b, num_18_b))
