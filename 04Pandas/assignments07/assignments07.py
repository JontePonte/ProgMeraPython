
# ***********************************
# Övningsuppgifter - Rensa data - hantera 'missing' data
# 



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



# Uppgift 2:
# Skriv ett program som tar bort alla 'NaN' och 'None' i kolumnen 'Bilmärke' i DataFrame-objektet
# 'df_beg_bilar'. Åtgärden ska vara permanent. 
# Skapa ett strängindexerat fält (lista) innehållande informationen om de begagnade bilarna:
 
beg_bilar = {'Bilmärke'   :['Volvo', 'BMW', 'AUDI', 'VW',   np.nan, 'NA',    None],
             'Färg'       :['NA'  ,  'Grå', 'Vit',  'Blå',  np.nan, 'Brun',  'Vit'],
             'Årsmodell'  :[ 2019,   2018,   2019,   2017,  None,    2018,   'Osäkert värde'],
             'Pris [tkr]' :[ 231,    None,   375,    255,   np.nan, 'NA',     195]}

df_beg_bilar = pd.DataFrame(beg_bilar) #Skapa ett DataFrame-objekt över 'beg_bilar'



# Uppgift 3:
# Skriv ett program som tar bort alla alla rader där samtliga kolumner innehåller 
# antingen 'NaN' eller 'None'.

# Skapa ett strängindexerat fält (lista) innehållande informationen om de begagnade bilarna:
 
beg_bilar = {'Bilmärke'   :['Volvo', 'BMW', 'AUDI', 'VW',   np.nan, 'NA',     None],
             'Färg'       :['NA'  ,  'Grå', 'Vit',  'Blå',  np.nan, 'Brun',   'Vit'],
             'Årsmodell'  :[ 2019,   2018,   2019,   2017,  None,    2018,    'Osäkert värde'],
             'Pris [tkr]' :[ 231,    None,   375,    255,   np.nan, 'NA',     195]}

df_beg_bilar = pd.DataFrame(beg_bilar) #Skapa ett DataFrame-objekt över 'beg_bilar'



# Uppgift 4:
# Skriv ett program som listar de kolumner i nedanstående DataFrame-objekt som innehåller 
# åtminstone 2 st 'NaN' och/eller 'None'. Använd metoden 'count'.

# Skapa ett strängindexerat fält (lista) innehållande informationen om de begagnade bilarna:
#  
beg_bilar = {'Bilmärke'   :['Volvo', 'BMW', 'AUDI', 'VW',   np.nan, 'NA',     None],
             'Färg'       :['NA'  ,  'Grå', 'Vit',  'Blå',  np.nan, 'Brun',  'Vit'],
             'Årsmodell'  :[ 2019,   2018,   2019,   2017,  None,    2018,   'Osäkert värde'],
             'Pris [tkr]' :[ 231,    None,   375,    255,   np.nan, 'NA',     195]}

df_beg_bilar = pd.DataFrame(beg_bilar) #Skapa ett DataFrame-objekt över 'beg_bilar'



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



# Uppgift 6:
# Skriv ett program som enbart stryker de rader som har 2 eller flera 'NaN' / 'None'. 
# Använd attributet 'thres' i metoden dropna.

#Skapa ett strängindexerat fält (lista) innehållande informationen om de begagnade bilarna: 

beg_bilar = {'Bilmärke'   :['Volvo', 'BMW', 'AUDI', 'VW',   np.nan, 'NA',     None],
             'Färg'       :['NA'  ,  'Grå', 'Vit',  'Blå',  np.nan, 'Brun',  'Vit'],
             'Årsmodell'  :[ 2019,   2018,   2019,   2017,  None,    2018,   'Osäkert värde'],
             'Pris [tkr]' :[ 231,    None,   375,    255,   np.nan, 'NA',     195]}

df_beg_bilar = pd.DataFrame(beg_bilar) #Skapa ett DataFrame-objekt över 'beg_bilar'




# Uppgift 7:
# Skriv ett program som stryker de kolumner som innehåller 'NaN' eller 'None'.
#Skapa ett strängindexerat fält (lista) innehållande informationen om de begagnade bilarna:

beg_bilar = {'Bilmärke'   :['Volvo', 'BMW', 'AUDI', 'VW',   np.nan, 'NA',     None],
             'Färg'       :['NA'  ,  'Grå', 'Vit',  'Blå',  np.nan, 'Brun',  'Vit'],
             'Årsmodell'  :[ 2019,   2018,   2019,   2017,  None,    2018,   'Osäkert värde'],
             'Pris [tkr]' :[ 231,    None,   375,    255,   np.nan, 'NA',     195]}

df_beg_bilar = pd.DataFrame(beg_bilar) #Skapa ett DataFrame-objekt över 'beg_bilar'
