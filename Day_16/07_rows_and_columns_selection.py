#Display column names.
import pandas as pd
students={
"name":["priyanka","pihu","anurag","aniket","arjun","davin"],
"age":[10,22,26,21,20,20],
"city":["Asia","America","Dubai","Shimla","Lahore","Pakistan"]}
var=pd.DataFrame(students)
#single column selection
print(var["age"])
#multiple column selection
print(var[["name","age"]])
#add a new column called salary
var["salary"]=[1000,2000,20000,20000,5000,4000]
print(var)
#rename a column
print(var.rename(columns={"salary": "sal_ary"}))

#delete a column
print()
var.pop("salary")
print(var)


#row selection
print(var.iloc[0])
#select rows 2 to 5
print(var.iloc[2:6])
#select last three rows
print(var.iloc[-3:])
#selects a row using its index label
print(var.loc[1])
#change the value of a specfic cell
var.loc[1,"age"]=99
print(var)