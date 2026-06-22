import numpy as np
arr=np.array([5,2,1,3,4,3,5,6])
filter=[]
for i in arr:
    if i in filter:
        print(i)
        break
    filter.append(i)
       