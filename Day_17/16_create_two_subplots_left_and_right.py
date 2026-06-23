import matplotlib.pyplot as plt
x = [1,2,3,4]
y=["data_1","data_2","data_3","data_4"]
plt.subplot(1,2,1)
plt.bar(x,y)
plt.subplot(1,2,2)
plt.pie(x,labels=y)
plt.show()