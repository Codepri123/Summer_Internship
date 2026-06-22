import pandas as pd
import numpy as np
data={
    "marks":[90,99,34],
    "age":[10,23,22]
}
var=pd.DataFrame(data)
print(var)
# var["grade">=90]
# print(var)
conditions = [var["marks"] >= 90, var["marks"] >= 75]
choices = ["A", "B", "C"]
var["Grade"] = np.select(conditions, choices, default="C")
print(var.drop(columns=["age"]))