# Find the number of rows and columns.
import pandas as pd
students={
"name":["priyanka","pihu","anurag","aniket","arjun","davin"],
"age":[10,22,26,21,20,20],
"city":["Asia","America","Dubai","Shimla","Lahore","Pakistan"]}
var=pd.DataFrame(students)
#Find the number of rows and columns.
print(var.shape)
print(var)