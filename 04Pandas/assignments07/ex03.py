'My solution to example 3 in the pandas module 03'

import pandas as pd
import numpy as np

# Uppgift 3:
# Skriv ett program som tar bort alla alla rader där samtliga kolumner innehåller 
# antingen 'NaN' eller 'None'.

# Skapa ett strängindexerat fält (lista) innehållande informationen om de begagnade bilarna:
 
beg_bilar = {'Bilmärke'   :['Volvo', 'BMW', 'AUDI', 'VW',   np.nan, 'NA',     None],
             'Färg'       :['NA'  ,  'Grå', 'Vit',  'Blå',  np.nan, 'Brun',   'Vit'],
             'Årsmodell'  :[ 2019,   2018,   2019,   2017,  None,    2018,    'Osäkert värde'],
             'Pris [tkr]' :[ 231,    None,   375,    255,   np.nan, 'NA',     195]}

df_beg_bilar = pd.DataFrame(beg_bilar) #Skapa ett DataFrame-objekt över 'beg_bilar'
df_beg_bilar.dropna(how='all', inplace=True)

print(df_beg_bilar)
