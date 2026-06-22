import pandas as pd
dict={
    "NAME":["PRIYANKA","ANIKET","ANUJ","ANURAG"],
    "MATH":[20 ,30,40,50],
    "SCIENCE":[100,200,300,400],
    "ENGLISH":[300,400,500,210]
    }
var=pd.DataFrame(dict)
print(var)
print()
#grade column added
var["GRADE"]=["A","B+","C","D"]
#MAXIMUM MARKS OF MATHS
print(var["MATH"].max())
#AVERAGE MARKS  OF EACH STUDENTS
var["AVERAGE"] = var[["MATH","SCIENCE","ENGLISH"]].mean(axis=1)
print(var[["NAME","AVERAGE"]])
var["TOTAL"]=var[["MATH","SCIENCE","ENGLISH"]].sum()
highest = var.loc[var["TOTAL"].idxmax()]
print(highest["NAME"])