import numpy as np
arr=np.array([18,1,2,3,4,5,12])
filter=[]
for i in arr:
    if i%2==0 and i%3==0:
        filter.append(True)
    else:
        filter.append(False)
print(arr[filter])        