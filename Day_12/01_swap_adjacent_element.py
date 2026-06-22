import numpy as np
arr=np.array([1,2,3,4,5,6])
arr_1=[]
print(arr)
for i in arr:
    for j in range(i+1,len(arr)+1,3):
         i,j=j,i
         if i==3 or i==5:
            break
         else:
          print(f"{i} swaps with {j}")
         arr_1.append(int(i))
         arr_1.append(int(j))
print(arr_1)          

