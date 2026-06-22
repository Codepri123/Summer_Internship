import numpy as np
arr = np.array([1, 2, 2, 3, 3, 3, 4],dtype="int")

count = {}

for i in arr:
    i=int(i)
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

print(count)