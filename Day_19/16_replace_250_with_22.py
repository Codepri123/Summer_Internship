import pandas as pd
data = {
    "Name":["Aniket","Rahul","Priya"],
    "Age":[21,250,20]
}
 
df = pd.DataFrame(data)
c=df.replace({"Age":250},22)
print(c)
