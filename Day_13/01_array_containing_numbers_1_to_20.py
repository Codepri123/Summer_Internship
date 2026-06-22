import numpy as np
arr= []
for i in range(1,21):
    arr.append(i)
    arr_2 = np.array(arr)
print(arr_2.shape)
print(arr_2.size)
print(arr_2.ndim)
print(arr_2.dtype)
