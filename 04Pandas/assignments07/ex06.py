'My solution for example 06 in pandas module 07'

import pandas as pd
import numpy as np

# Uppgift 6:
# Skriv ett program som enbart stryker de rader som har 2 eller flera 'NaN' / 'None'. 
# Använd attributet 'thres' i metoden dropna.

#Skapa ett strängindexerat fält (lista) innehållande informationen om de begagnade bilarna: 
beg_bilar = {'Bilmärke'   :['Volvo', 'BMW', 'AUDI', 'VW',   np.nan, 'NA',     None],
             'Färg'       :['NA'  ,  'Grå', 'Vit',  'Blå',  np.nan, 'Brun',  'Vit'],
             'Årsmodell'  :[ 2019,   2018,   2019,   2017,  None,    2018,   'Osäkert värde'],
             'Pris [tkr]' :[ 231,    None,   375,    255,   np.nan, 'NA',     195]}

df_beg_bilar = pd.DataFrame(beg_bilar) #Skapa ett DataFrame-objekt över 'beg_bilar'

# Nicer solution if all values that really has NaN is included
df_beg_bilar.replace({'NA': np.nan, 'Osäkert värde': np.nan, None: np.nan}, inplace=True)
# print(df_beg_bilar)

df_beg_bilar.dropna(thresh=df_beg_bilar.shape[1]-1, inplace=True)
print(df_beg_bilar)
