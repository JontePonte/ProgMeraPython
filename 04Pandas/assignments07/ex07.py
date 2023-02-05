'My solution for example 07 in pandas module 07'

import pandas as pd
import numpy as np

# Uppgift 7:
# Skriv ett program som stryker de kolumner som innehåller 'NaN' eller 'None'.

# Skapa ett strängindexerat fält (lista) innehållande informationen om de begagnade bilarna:
beg_bilar = {'Bilmärke'   :['Volvo', 'BMW', 'AUDI', 'VW',   np.nan, 'NA',     None],
             'Färg'       :['NA'  ,  'Grå', 'Vit',  'Blå',  np.nan, 'Brun',  'Vit'],
             'Årsmodell'  :[ 2019,   2018,   2019,   2017,  None,    2018,   'Osäkert värde'],
             'Pris [tkr]' :[ 231,    None,   375,    255,   np.nan, 'NA',     195]}

df_beg_bilar = pd.DataFrame(beg_bilar) #Skapa ett DataFrame-objekt över 'beg_bilar'

df_beg_bilar.dropna(axis='columns', inplace=True)
print(df_beg_bilar) # A bit weird question because all columns include NaN or None
