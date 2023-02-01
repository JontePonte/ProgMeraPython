
import pandas as pd


temperature_data = pd.read_csv('04Pandas/assignments05/temp_falsterbo_froson.csv')


# Uppgift 7:
# Skriv ett program som listar en sammanställning för temepraturen med avseende 
# på medelvärde-, största- och minsta värden för Falsterbo under juli 2019.
filt = (temperature_data['Datum'] >= '2019-07-01') & (temperature_data['Datum'] <= '2019-07-31')
print(temperature_data[filt][['Datum','Falsterbo']].describe())


# Uppgift 8:
# Skriv ett program som listar de dagar under 2019 när temperaturen på Frösön 
# är högre än +25C




# Uppgift 9:
# Skriv ett program som listar de dagar under maj, juni, juli, augusti år 2019 
# när temperaturen på Frösön är högre än temperaturen i Falsterbo.