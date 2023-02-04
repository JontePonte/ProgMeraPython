'My solution to example 01 in pandas module 07'

import pandas as pd
import numpy as np

# Uppgift 1:
# Skriv ett program som listar alla de rader i kolumnen 'Pris [tkr]' hos DataFrame-objektet 
# 'df_beg_bilar' som innehåller 'NaN' eller 'None' 
# Skapa ett strängindexerat fält (lista) innehållande informationen om de begagnade bilarna:
 
beg_bilar = {'Bilmärke'   :['Volvo', 'BMW', 'AUDI', 'VW',   np.nan, 'NA', None],
             'Färg'       :['NA'  ,  'Grå', 'Vit',  'Blå',  np.nan, 'Brun', 'Vit'],
             'Årsmodell'  :[ 2019,   2018,   2019,   2017,  None,    2018, 'Osäkert värde'],
             'Pris [tkr]' :[ 231,    None,   375,    255,   np.nan, 'NA',     195]}

df_beg_bilar = pd.DataFrame(beg_bilar) #Skapa ett DataFrame-objekt över 'beg_bilar'

print(df_beg_bilar)
