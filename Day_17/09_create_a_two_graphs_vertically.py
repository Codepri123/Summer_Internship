import matplotlib.pyplot as plt
import numpy as np
expenses=np.arange(1000,1012)
months=np.array(["january","feburay","March","april","may","june","july","august","sept","OCT","NOVEMBER","DECEMBER"])
plt.subplot(2,1,1)
plt.plot(expenses,months ,marker="^")
plt.subplot(2,1,2)
plt.bar(expenses,months)
plt.show()