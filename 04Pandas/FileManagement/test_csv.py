'Fooling around with pandas file management system'

import pandas as pd

# A nice way to read the file don't you say
df = pd.read_csv(
    '04Pandas/FileManagement/artikel_data.csv',
    sep=';',
    encoding='latin_1',
    index_col='Art. Nr',
    )
print(df)

filt = df['Artikel'] == 'Skruv'

df_skruv = df[filt]
print(df_skruv)

df_skruv.to_csv(
    '04Pandas/FileManagement/skruv_data.csv',
    sep=';',
    encoding='latin_1',
    )
