import matplotlib.pyplot as plt
x = [1,2,3,4]
y=["data_1","data_2","data_3","data_4"]
plt.subplot(2,2,1)
plt.plot(x,y)
plt.subplot(2,2,2)
plt.scatter(x,y)
plt.subplot(2,2,3)
plt.hist(x)
plt.subplot(2,2,4)
plt.pie(x,labels=y)
plt.show()