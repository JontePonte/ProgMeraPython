import pandas as pd


# a little tricky but I remember it from before. 
# I need to add the folder structure because python is run from the root folder
temperature_data = pd.read_csv('04Pandas/assignments05/temp_falsterbo_froson.csv')


# Uppgift 1:
#Skriv en programrad som listar antal rader och kolumner hos 'temperatur_data'
# print(f"The data has {temperature_data.shape[0]} rows and {temperature_data.shape[1]} columns")


# Uppgift 2:
#Skriv ett program som listar de första 15 raderna och de sista 15 raderna i 'temperatur_data'
# print(temperature_data.iloc[0:15])
# print(temperature_data.iloc[-15:])


# Uppgift 3:
# Skriv ett program som gör en sammanställning av innehållet i 
# 'temperatur_data' med avseende på antal data, medelvärde, min- och max- värde
print(temperature_data.info())

