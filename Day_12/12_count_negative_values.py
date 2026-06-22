import numpy as np
arr=np.array([1,2,-1,-5])
filter=[]
count=0
for i in arr:
    if i<0:
        filter.append(True)
        count+=1
    else:
        filter.append(False)
print(arr[filter]) 
print(count)       
