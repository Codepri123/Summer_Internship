# Find employees with salary greater than 50,000.
#Create a DataFrame with columns Name, Age, and City.
import pandas as pd
students={
"name":["priyanka","pihu","anurag","aniket"],
"age":[10,22,26,21],
"city":["Asia","America","Dubai","Shimla"],
"salary":[10000,20000,30000,40000]}
var=pd.DataFrame(students)
print(var[(var["city"]=="Dubai")])
#Find rows where Department is either IT or HR
print(var[("city"=="Dubai" or var["city"]=="Asia")])

