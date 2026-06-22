import numpy as np
arr=np.array([21,21,2,-1,-5])
filter=[]
for i in arr:
    if i not in filter:
        filter.append(int(i))
    else:
        pass
print((filter))   
     