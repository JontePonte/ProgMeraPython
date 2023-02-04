'My solution to example 05 in pandas module 07'

import pandas as pd
import numpy as np

# Uppgift 5:
# Skriv ett program som byter ut 'NA' och 'Osäkert värde' i nedanstående 
# DataFrame-objekt mot 'NA' och 'Osäkert värde' mot 'np.nan'. 

# Använd metoden replace med inargumentet bestående av den data som ska ersättas uttryckt 
# som ett strängindexerat fält.

# Skapa ett strängindexerat fält (lista) innehållande informationen om de begagnade bilarna:
beg_bilar = {'Bilmärke'   :['Volvo', 'BMW', 'AUDI', 'VW',   np.nan, 'NA',     None],
             'Färg'       :['NA'  ,  'Grå', 'Vit',  'Blå',  np.nan, 'Brun',   'Vit'],
             'Årsmodell'  :[ 2019,   2018,   2019,   2017,  None,    2018,   'Osäkert värde'],
             'Pris [tkr]' :[ 231,    None,   375,    255,   np.nan, 'NA',     195]}

df_beg_bilar = pd.DataFrame(beg_bilar) #Skapa ett DataFrame-objekt över 'beg_bilar'

# Added None: np.nan to make the output more uniform
df_beg_bilar.replace({'NA': np.nan, 'Osäkert värde': np.nan, None: np.nan}, inplace=True)

print(df_beg_bilar)
