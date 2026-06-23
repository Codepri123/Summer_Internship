import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

students = {
    "name": ["priyanka", "pihu", "anurag", "aniket", "arjun", "davin"],
    "age": [10, 22, 26, 21, 20, 20],
    "city": ["Asia", "America", "Dubai", "Shimla", "Lahore", "Pakistan"]
}
var = pd.DataFrame(students)
print(var)
plt.plot(var["name"], var["age"],linestyle="--" ,color="green",linewidth=4, marker='o')
plt.xlabel("Name")
plt.ylabel("Age")
plt.title("Students Age Chart",color="red",size=20)
plt.grid(axis='x',color="red",linestyle="--",linewidth=2)
plt.grid(axis='y',color="blue",linewidth=2,linestyle="--")

plt.show()