import pandas as pd
import numpy as np

data = {
    "Math": [20, np.nan, 40, 50],
    "Science": [100, 200, np.nan, 400],
    "English": [300, np.nan, np.nan, 210]
}

df = pd.DataFrame(data)

print(df)
#finding missing values
print(df.isnull().sum())
#replace missing values with column mean
print(df.fillna(df.mean()))
print(df.dropna(thresh=1))