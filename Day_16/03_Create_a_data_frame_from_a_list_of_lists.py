# Create a DataFrame from a list of lists.
import pandas as pd
lst=[1,2,3,[4,5,6]]
flat=[]
for i in lst:
     if isinstance(i, list):
      for j in i:
        flat.append(j)
      else:
         flat.append(i)
print(flat)        
var=pd.DataFrame(flat,columns=["Values"])
print(var)