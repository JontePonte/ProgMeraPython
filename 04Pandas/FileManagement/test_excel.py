'Messing around with pandas read and wright to excel'

import pandas as pd

df = pd.read_excel(
    '04Pandas/FileManagement/artikel_data.xlsx',
    index_col='Art. Nr',
    )

print(df)
