
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 09:49:37 2022
@author: Hosh
"""
import numpy as np

# 1. Skriv ett pythonprogram som använder modulen NumPy och generear följande 
# NumPy-array:

a = [[ 0,  1,  2,  3,  4],
    [ 1,  2,  3,  4,  5],
    [ 4,  5,  6,  7,  8],
    [ 9, 10, 11, 12, 13],
    [16, 17, 18, 19, 20]]

print(np.__version__)

# 2. Skriv ett pythonprogram som använder NumPy-modulen för att 
# generera en talföjld av 20 slumpmässiga tal och omvandlar dessa till
# en matris med 5 rader och 4 kolumner som skrivs ut. Därefter placeras de element 
# i NumPy-arrayen som är större än -0.5 i en ny array och skrivs ut.




# 3. Skriv ett pythonprogram som använder modulen NumPy och generear följande 
# NumPy-array och därfter beräknar differensen mellan NumPy-array och dess 
# transponat:

# Vilken typ av NumPy-array(matris) får man som resultat?

A=[[0,  1,  2,  3,  4],
 [ 1,  2,  3,  4,  5],
 [ 4,  5,  6,  7,  8],
 [ 9, 10, 11, 12, 13],
 [16, 17, 18, 19, 20]]




# 4. Skapa ett pythonprogram som genererar matrisen
# och skriver ut de element i NumPy-array som är mindre än 5.
A = [[[1, 2, 3],
[4, 5, 6]],
[[7, 8, 9],
[10, 11, 12]]]





# 5. Skriv ett program som skapar och skriver ut följande matris: 
A = [[0.,  0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],
 [1.,  1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9],
 [2.,  2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9],
 [3.,  3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9],
 [4.,  4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9],
 [5.,  5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9],
 [6.,  6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 6.9],
 [7.,  7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7, 7.8, 7.9],
 [8.,  8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 8.8, 8.9],
 [9.,  9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 9.9],]



# 6. Skapa en Pythonprogram som genererar
A = [[[1, 2, 3, 4],
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
# genom att använda operatorn %=.



# 7. Låt  
A=[[0.,  0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],
   [1.,  1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9],
   [2.,  2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9],
   [3.,  3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9],
   [4.,  4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9],
   [5.,  5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9],
   [6.,  6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 6.9],
   [7.,  7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7, 7.8, 7.9],
   [8.,  8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 8.8, 8.9],
   [9.,  9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 9.9],]
# och därefter extrahera följande element i A genom att använda slicing metoden
# [[0.3 0.7]
#  [4.3 4.7]]



# 8. Skapa följande lista: 
A = [0,4,8, 12, 16, 20, 24,
 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72,
 76, 80, 84, 88, 92, 96]

# och omvandla denna till följande NumPy-array:
# [[ 0  4  8 12 16]
#  [20 24 28 32 36]
#  [40 44 48 52 56]
#  [60 64 68 72 76]
#  [80 84 88 92 96]]
# Extrahera därefter följande element ur Numpy-arrayen 
# [[44 48 52]
#  [64 68 72]]



# 9. Skapa följande två NumPy-arrayer:
A = [[ 0,  1,  2,  3,  4],
 [ 5,  6,  7,  8,  9],
 [10, 11, 12, 13, 14],
 [15, 16, 17, 18, 19],
 [20, 21, 22, 23, 24],]

B = [[20, 21, 22, 23, 24],
 [25, 26, 27, 28, 29],
 [30, 31, 32, 33, 34],
 [35, 36, 37, 38, 39],
 [40, 41, 42, 43, 44],]
# Skriv därefter ut alla gemensamma element i de två NumPy-arrayerna.



# 10. Skapa en slumpad NumPy-array med med värden mellan 2 och 15 och följande 
# form och omvandla denna till en vektor (1d NumPy-array).
    
A = [[12, 11,  2,  6, 12],
 [ 9, 14, 11, 13, 11],
 [11, 13,  8, 12, 10],
 [ 3,  9,  5, 13, 11],
 [ 3,  9,  7, 10,  9],
 [ 8,  8,  2,  5, 12],
 [ 8,  5, 10,  6,  2],
 [13,  6,  4,  7,  4],
 [ 6,  2,  5,  9, 10],
 [10,  5,  3, 10,  2],]



# 11. Skapa en slumpad NumPy-array med med värden mellan 20 och 135 och följande 
#     form och  och skriv ut maxvärdet i varje rad respektive kolumn.
A = [[ 46, 125,  36,  88,  62],
 [ 75,  96,  99, 109,  34],
 [111,  77, 109,  31,  26],
 [ 62,  76,  21,  27,  71],
 [ 47,  93,  35,  21, 130],
 [ 43, 105,  44,  27,  42],
 [ 74,  97,  36, 126,  90],
 [ 55,  51,  52,  65,  79],
 [ 65,  81,  40, 134, 105],
 [134,  20,  23,  75, 115],
 [ 76,  23,  53,  92,  20],
 [ 72, 110,  81,  90,  98],]


# 12. Använd Binets formel 
#     fn=[((1+5^1/2)/2)^n-((1-5^1/2)/2)^n]*(1/5^1/2)
#     för att räkna de 15 första talen i Fibonacci talföjlden.



# 13. Skriv en program som skapar nedanstående Numpy-array 
#     och därfter använder Numpys inbyggda funktioner add(), multiply(), subtract() 
# och divide() för att beräkna 
#     summan, produkten, skillnaden och kvoten av A och B.
A = [[ 1,  2,  3,  4],
 [ 5,  6,  7,  8],
 [ 9, 10, 11, 12],
 [13, 14, 15, 16],]

B = [[11, 12, 13, 14],
 [15, 16, 17, 18],
 [19, 20, 21, 22],
 [23, 24, 25, 26],]



# 14. Använda Numpy funktion where() för att omvandla följande Numpy-array:
A = [[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9],]

# till Numpy-arrayen:
# [[ 1  2  3]
#  [ 4  5 12]
#  [12 12 12]]



# 15. Man kan använda  funktionen array_split() för dela en Numpy-array till olika 
# sub Numpy-arrayer. 
# Använd denna funktion för att skapa 5 sub Numpy-array från:
A = [[ 1,  2,  3,  4,  5,  6,  7],
 [ 8,  9, 10, 11, 12, 13, 14],
 [15, 16, 17, 18, 19, 20, 21],
 [22, 23, 24, 25, 26, 27, 28],
 [29, 30, 31, 32, 33, 34, 35],
 [36, 37, 38, 39, 40, 41, 42],
 [43, 44, 45, 46, 47, 48, 49],]



# 16. Skapa följande Numpy-array
A=[ 6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 11, 11, 11, 11, 11]
# genom att använda funktionen where() från Nympy-arrayen:
B=[ 6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26] 

# (se uppgift 16)
# och därfter hitta positionen för talet 11 i A med hjälp av samma funktion. 



# 17. Använda  sort() funktionen för att sortera Numpy-array:
#     ['Röd', 'Grön', 'Vitt', 'Svart','Lilla','Gull', 'violet','Mörkröd','Blå']
#     och skriv därefter ut positionen för 'Svart' före och efter sorteringen.



# 18. Skriv ett program som använder funktionerna lcm() och gcd() för att beräkna
#     minsta gemensamma multipel och största gemensamma nämnare av två tal som du 
# matar in.


