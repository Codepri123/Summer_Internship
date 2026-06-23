import matplotlib.pyplot as plt
import numpy as np
temp=[20,30,40,50,60,70]
days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
plt.barh(temp,days ,color="green" ,height=5)
plt.show()