import numpy as np
number=np.array([11,22,33,44,55,66,77,88])
filter_arr=[]
for i in number:
    if i%2==0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
new_arr=number[filter_arr]  
print(new_arr) 
print(filter_arr)     