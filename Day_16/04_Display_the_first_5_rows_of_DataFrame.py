# Display the first 5 rows of a DataFrame.
import pandas as pd
students={
"name":["priyanka","pihu","anurag","aniket","arjun","davin"],
"age":[10,22,26,21,20,20],
"city":["Asia","America","Dubai","Shimla","Lahore","Pakistan"]}
var=pd.DataFrame(students)
#first five rows of a Data Frame
print(var.head())