import numpy as np
# [1,2,3,4] → [2,3,4,1]
arr=np.array([1,2,3,4])
d=1
a=arr[d:]
b=arr[:d]

z=np.concatenate((a,b),axis=0)
print(z)
# NO slicing, NO built-in functions
import numpy as np

arr = np.array([1, 2, 3, 4])

n = len(arr)

first = arr[0]

for i in range(n - 1):
    arr[i] = arr[i + 1]

arr[n - 1] = first

print(arr)

