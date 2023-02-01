
import pandas as pd

# Uppgift 11:
# Skriv ett program som elementvis jämför nedanstående Series-objekt oh skriver ut 
# 1) identiska element
# 2) de element i 'ds_1' som är större än elementen i 'ds_2', 3) de element som 
# är olika
ds_1 = pd.Series([2, 3, 6, 4, 10])
ds_2 = pd.Series([1, 3, 5, 7, 10])



# Uppgift 12:
# Nedanstående strängindexerat fält innehåller resultatet från en försökserie med 
# 4 olika preparat
# 'A', 'B', 'C' och deras uppmätta styrka. 1) Skapa ett DataFrame-objekt av 
# det strängindexerade fältet och gruppera resultaten och 2) beräkna och skriv ut medelvärde,
# standardaavikelse, minsta- och största värde för varje preparat. Utifrån det beräknade 
# resultet är det något/några värden som 
# 'sticker ut'? Ge i så fall en möjlig förklaring.

test_serie = {
    'Preparat': ['A', 'C', 'B', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'C', 'B', 'A', 'B'],
    'Styrka'  : [12.4, 5.3, 9.2, 8.9, 3.1, 6.4, 10.1, 5.9, 1.8, 4.9, 5.6, 9.0, 1.9, 8.6]}

print(test_serie)
