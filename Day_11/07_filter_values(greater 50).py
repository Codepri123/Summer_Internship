import numpy as np
#filter values greater than 50
arr=np.array([1,2,3,4,50,60,70])
filter=[]
for i in arr:
    if i>50:
        filter.append(True)
    else:
        filter.append(False)
print(arr[filter])        