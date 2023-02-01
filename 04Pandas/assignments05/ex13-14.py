
import pandas as pd

# Uppgift 13:
# Skriv ett program som byter ut alla 'A' i DataFrame-objektet 'df' mot 'Ö' och 
# 4 mot 40.

df = pd.DataFrame([[1, 'A'], [2, 'B'],[3, 'A'],[4, 'C'], [3, 'A'],[4, 'D']], 
columns=['K1', 'K2'])



# Uppgift 14:
# Skriv ett program som stryker alla rader som innehåller bokstaven 'A' i 
# DataFrame-objektet 'df_1' och sparar resultatet i en nytt DataFrane-objekt 'df_2'.

df_1 =pd.DataFrame([[1, 'A'], [2, 'B'],[3, 'A'],[4, 'C'], [3, 'A'],[4, 'D']], 
columns=['K1', 'K2'])
