import numpy as np
#Filter names starting with "A".
arr=np.array(["arjun","arnav","priyanka","aniket","ARAV"])
filter=[]
for i in arr:
         if i.startswith("a") or i.startswith("A"):
          filter.append(True)
         else:
          filter.append(False)
print(arr[filter])   