import numpy as np
arr=np.array([1,2,3,4])
arr_1=[]
for i in range(len(arr)-1,-1,-1):
   arr_1.append(int(arr[i]))
print(arr_1)   
if np.array_equal(arr_1, arr):
   print("It is a palindrome")
else:
   print("It is not a palindrome")