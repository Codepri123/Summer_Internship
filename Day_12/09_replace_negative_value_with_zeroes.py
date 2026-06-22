import numpy as np
arr=np.array([-1,-2,34,56])
for i in range(len(arr)):
     if arr[i] < 0:
        arr[i] = 0
     else:
         pass
print(arr)
       