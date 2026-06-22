import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr.shape)

# a=arr[0:1:1]
# b=arr[1:2:1]
# c=arr[2:3:1]
# d=a.flatten()
# e=b.flatten()
# f=c.flatten()
# print(d,e,f)
# x=d[::-1]
# y=e[::-1]
# z=f[::-1]
# print(x,y,z)
a=arr.flatten()
b=a[::-1]
print(b)
c= b.reshape(3,3)
print(c[::-1])
