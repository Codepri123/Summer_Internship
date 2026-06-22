#Display column names.
import pandas as pd
students={
"name":["priyanka","pihu","anurag","aniket","arjun","davin"],
"age":[10,22,26,21,20,20],
"city":["Asia","America","Dubai","Shimla","Lahore","Pakistan"]}
var=pd.DataFrame(students)
print(var.columns)
print(var.dtypes)
#summary statistics of numerical columns
print(var.describe())