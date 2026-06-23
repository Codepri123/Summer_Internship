#create a graph of showing monthly expenses 
import matplotlib.pyplot as plt
import numpy as np
expenses=np.arange(1000,1012)
months=np.array(["january","feburay","March","april","may","june","july","august","sept","OCT","NOVEMBER","DECEMBER"])
plt.title("expenses chart")
plt.xlabel("expenses")
plt.ylabel("months")
plt.plot(expenses,months ,marker="s",markersize=15)
plt.show()