

#!/usr/bin/env python
# coding: utf-8
# 
# ***********************************************************************************
# Övningsuppgifter - Filtrera och gruppera data
# 
# ***********************************************************************************
import pandas as pd
# 
# ***********************************************************************************

# OBS! För att lösa övningsuppgifterna skall datafilen 'temp_falsterbo_froson.csv' 
# användas. Datafilen finns sparad i Canvas. Kopiera den sedan till det biblioteket 
# där denna JN-fil finns.Den innehåller temperaturdata från väderstationerna i 
# Falsterbo och Frösön uppmätt varje dag kl. 12.00 från 2018-01-01 -- 2019-12-31.
# Nedanstående programrad läser in datat i variabeln 'temperatur_data'

temperatur_data = pd.read_csv('temp_falsterbo_froson.csv')


# Uppgift 1:
#Skriv en programrad som listar antal rader och kolumner hos 'temperatur_data'




# Uppgift 2:
#Skriv ett program som listar de första 15 raderna och de sista 15 raderna i 'temperatur_data'



# Uppgift 3:
# Skriv ett program som gör en sammanställning av innehållet i 
# 'temperatur_data' med avseende på antal data, medelvärde, min- och max- värde



# Uppgift 4:
# Skriv ett program som skriver ut de första två temperaturvärdena för Frösön 



# Uppgift 5:
# Skriv ett program som skriver ut temperaturerna i Falsterbo och på Frösön 
# under 4 slumässiga dagar.



# Uppgift 6:
#Skriv ett program som listar alla temperaturer på Frösön under januari 2018. 




# Uppgift 7:
# Skriv ett program som listar en sammanställning för temepraturen med avseende 
# på medelvärde-, största- och minsta värden för Falsterbo under juli 2019.




# Uppgift 8:
# Skriv ett program som listar de dagar under 2019 när temperaturen på Frösön 
# är högre än +25C




# Uppgift 9:
# Skriv ett program som listar de dagar under maj, juni, juli, augusti år 2019 
# när temperaturen på Frösön är högre än temperaturen i Falsterbo.




# Uppgift 10:
# Hur många grader skiljde sig medeltemperaturen mellan Fröson och Falsterbo 
# under december månad 2018?




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



# Uppgift 13:
# Skriv ett program som byter ut alla 'A' i DataFrame-objektet 'df' mot 'Ö' och 
# 4 mot 40.

df = pd.DataFrame([[1, 'A'], [2, 'B'],[3, 'A'],[4, 'C'], [3, 'A'],[4, 'D']], 
columns=['K1', 'K2'])



# Uppgift 14:
# Skriv ett program som stryker alla rader som innehåller bokstaven 'A' i 
# DataFrame-objektet 'df_1' och sparar resultatet i en nytt DataFrane-objekt 'df_2'.

df_1 =pd.DataFrame([[1, 'A'], [2, 'B'],[3, 'A'],[4, 'C'], [3, 'A'],[4, 'D']], 
columns=['K1', 'K2'])
