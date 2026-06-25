import pandas as pd
df1 = pd.DataFrame({"Name": ["A", "B"]}, index=[1,2])
df2 = pd.DataFrame({"Age": [20]}, index=[1])
x=df1.join(df2)
print(x)


