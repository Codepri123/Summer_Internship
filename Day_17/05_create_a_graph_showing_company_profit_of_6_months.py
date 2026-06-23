import matplotlib.pyplot as plt
import numpy as np
plt.title("COMPANY PROFIT FOR 6 MONTHS")
months=np.array(["january","feburay","March","april","may","june"])
cost=[10000,-20,30,10000000,30000,78]
expenses=[]
for i in cost:
    if cost not in expenses:
     expenses.append(i)
    else:
       pass
print(expenses)   
plt.plot(expenses,months)  
plt.show()  