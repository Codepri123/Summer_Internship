import pandas as pd
data = {
    "Name":["Aniket","Rahul","Priya"],
    "Age":[21,250,20]
}
 
df = pd.DataFrame(data)
df = df[df["Age"] != 250]

print(df)