# import numpy as np

# arr = np.array([1, 2, 3, 4, 5])

# # Without using loops:
# # 1. Square each element
# # 2. Keep only even squares
# # 3. Find their sum

import numpy as np
def square(arr):
    if arr%2==0:
     return arr**2
    else:
      return 0
sq=np.frompyfunc(square,1,1)
print(sq(([1, 2, 3, 4, 5])))


