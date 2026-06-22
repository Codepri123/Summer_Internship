import numpy as np
#Filter negative numbers.
arr=np.array([-1,-2,-3,4,50,60,-70])
filter=[]
for i in arr:
    if i<0:
        filter.append(True)
    else:
        filter.append(False)
print(arr[filter])   
arr=np.array([-1,-2,-3,4,50,60,-70])
filter=[]
for i in arr:
    if i<0:
        filter.append(True)
    else:
        filter.append(False)
print(arr[filter])   