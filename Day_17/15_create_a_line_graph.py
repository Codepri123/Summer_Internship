import matplotlib.pyplot as plt
x = [1,2,3,4]
y = [5,10,15,20]
plt.plot(x,y,color="red",linestyle="--",linewidth=3,marker="o")
plt.title("graph")
plt.grid()
plt.xlabel("x value")
plt.ylabel("y value")
plt.show()