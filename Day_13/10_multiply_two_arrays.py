import numpy as np
def multiply(arr_1,arr_2):
    return arr_1*arr_2
multiply=np.frompyfunc(multiply,2,1)
print(multiply(np.array([10,20,40,50,60]),np.array([50,40,10,20,1])))