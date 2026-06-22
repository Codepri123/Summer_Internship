#Create a DataFrame with columns Name, Age, and City.
import pandas as pd
students={
"name":["priyanka","pihu","anurag","aniket"],
"age":[10,22,26,21],
"city":["Asia","America","Dubai","Shimla"]}
var=pd.DataFrame(students)
print(var)