
import pandas as pd
import random

temperature_data = pd.read_csv('04Pandas/assignments05/temp_falsterbo_froson.csv')

# Uppgift 4:
# Skriv ett program som skriver ut de första två temperaturvärdena för Frösön 
# print(temperature_data.iloc[0:2, [0,3]])


# Uppgift 5:
# Skriv ett program som skriver ut temperaturerna i Falsterbo och på Frösön 
# under 4 slumässiga dagar.

# My naive solution. Quite fancy with list comprehension
rows = temperature_data.shape[0]
rand_num = [random.randint(0,rows) for _ in range(4)]
# print(temperature_data.iloc[rand_num])

# print(temperature_data.sample(4))


# Uppgift 6:
#Skriv ett program som listar alla temperaturer på Frösön under januari 2018.

# This is a important one to get...
filt = (temperature_data['Datum'] >= '2018-01-01') & (temperature_data['Datum'] <= '2018-01-31')
print(temperature_data[filt][["Datum", "Froson"]])
