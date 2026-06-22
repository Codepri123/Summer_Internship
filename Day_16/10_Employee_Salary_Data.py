import pandas as pd
data={
    "NAME":["PRIYANKA","ANIKET","ANUJ","ANURAG"],
    "DEPARTMENT":["PHYSICS","CHEMISTRY","SCIENCE","MATHEMATICS"],
    "SALARY":[10000,200000,30000,40000]
}
var=pd.DataFrame(data)
print(var)
print(var["SALARY"].value_counts())
print(var)