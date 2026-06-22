import numpy as np
def square(arr):
    return arr**2
square=np.frompyfunc(square,1,1)
print(square(np.array([1, 2, 3, 4, 5])))
