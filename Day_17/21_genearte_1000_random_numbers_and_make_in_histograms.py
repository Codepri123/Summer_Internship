import matplotlib.pyplot as plt
import numpy as np
a=np.random.randint(1,100,1000)
plt.hist(a,bins=5)
plt.show()