import matplotlib.pyplot as plt
import numpy as np
expenses=np.arange(1000,1012)
color=np.random.choice(['red','orange'],12)
print(color)
months=np.array(["january","feburay","March","april","may","june","july","august","sept","OCT","NOVEMBER","DECEMBER"])
plt.title("expenses chart")
plt.xlabel("expenses")
plt.ylabel("months")
plt.scatter(expenses,months,color=color)
plt.show()