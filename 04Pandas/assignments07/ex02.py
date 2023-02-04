'My solution to example02 in pandas module 07'

import pandas as pd
import numpy as np

# Uppgift 2:
# Skriv ett program som tar bort alla 'NaN' och 'None' i kolumnen 'Bilmärke' i DataFrame-objektet
# 'df_beg_bilar'. Åtgärden ska vara permanent. 
# Skapa ett strängindexerat fält (lista) innehållande informationen om de begagnade bilarna:
 
beg_bilar = {'Bilmärke'   :['Volvo', 'BMW', 'AUDI', 'VW',   np.nan, 'NA',    None],
             'Färg'       :['NA'  ,  'Grå', 'Vit',  'Blå',  np.nan, 'Brun',  'Vit'],
             'Årsmodell'  :[ 2019,   2018,   2019,   2017,  None,    2018,   'Osäkert värde'],
             'Pris [tkr]' :[ 231,    None,   375,    255,   np.nan, 'NA',     195]}

df_beg_bilar = pd.DataFrame(beg_bilar) #Skapa ett DataFrame-objekt över 'beg_bilar'

