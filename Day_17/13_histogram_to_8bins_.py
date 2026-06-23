import matplotlib.pyplot as plt
import numpy as np
marks=np.array([20,30,100,90,80,70,60,50,40,10,5,6])
plt.hist(marks ,bins=8,color="green",edgecolor="black")
plt.grid()
plt.show()