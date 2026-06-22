import numpy as np
arr=np.array([1,2,4,5,6])
a=arr[:-2]
b=arr[-2:]
print(b,a)
arr_1 =np.concatenate((b,a),axis=0)
print(arr_1)
