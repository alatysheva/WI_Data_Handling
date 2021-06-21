import lasio
import pandas as pd
data = pd.read_csv('123.csv')
df1 = pd.DataFrame(data)
for col in df1.columns:
    if str(col).lower().find(r'tim') != -1:
        df1 = df1.drop(col, axis=1)
        pass

df1 = df1.reset_index(drop=True)
print(df1.columns)