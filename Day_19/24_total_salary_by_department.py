import pandas as pd
df = pd.DataFrame({
    "Dept":["IT","HR","IT","HR"],
    "Salary":[50000,40000,60000,45000]
})

x=df.groupby("Dept")["Salary"].agg(["mean","sum","count"])
print(x)
