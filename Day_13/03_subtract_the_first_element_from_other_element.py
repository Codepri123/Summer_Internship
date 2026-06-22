import numpy as np
def subtract(arr):
    return arr-10
subtract=np.frompyfunc(subtract,1,1)
print(subtract( np.array([10, 20, 30, 40, 50])))