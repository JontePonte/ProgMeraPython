'My solution of example 04 in pandas module 07'

import pandas as pd
import numpy as np

# Uppgift 4:
# Skriv ett program som listar de kolumner i nedanstående DataFrame-objekt som innehåller 
# åtminstone 2 st 'NaN' och/eller 'None'. Använd metoden 'count'.

# Skapa ett strängindexerat fält (lista) innehållande informationen om de begagnade bilarna:
beg_bilar = {'Bilmärke'   :['Volvo', 'BMW', 'AUDI', 'VW',   np.nan, 'NA',     None],
             'Färg'       :['NA'  ,  'Grå', 'Vit',  'Blå',  np.nan, 'Brun',  'Vit'],
             'Årsmodell'  :[ 2019,   2018,   2019,   2017,  None,    2018,   'Osäkert värde'],
             'Pris [tkr]' :[ 231,    None,   375,    255,   np.nan, 'NA',     195]}

df_beg_bilar = pd.DataFrame(beg_bilar) #Skapa ett DataFrame-objekt över 'beg_bilar'

filt = df_beg_bilar.count() <= df_beg_bilar.shape[0] - 2 

print(filt)
