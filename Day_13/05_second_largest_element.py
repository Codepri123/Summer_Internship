import numpy as np
arr = np.array([10, 20, 300, 200, 15])
#first largest number
largest = arr[0]
for i in arr:
    if i > largest:
        largest = i
print("The largest number is :",largest)        
arr = arr[arr != largest]
#second largest number
second_largest = arr[0]
for j in arr:
    if j > second_largest:
        second_largest = j

arr = arr[arr != second_largest]
print("The second largest number is :",second_largest)
#third largest number
third_largest = arr[0]
for k in arr:
    if k > third_largest:
        third_largest = k
print("The third largest number is :",third_largest)
