import numpy as np
arr=np.array([1,2,3,4,6,7,8])
arr_1=max(arr)*(max(arr)+1)//2
arr_2=arr_1-sum(arr)
print("The missing number is ",arr_2)
