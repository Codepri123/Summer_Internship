import matplotlib.pyplot as plt
import numpy as np
temp=[20,30,40,50,60,70]
days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
plt.plot(temp,days ,linestyle="--" ,color="red")
plt.bar(temp,days )
plt.show()
