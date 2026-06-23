import matplotlib.pyplot as plt
students=["A","B","C","D","E"]
marks=[65,20,100,30,70]
plt.title("line chart")
plt.plot(students,marks)
plt.show()
plt.title("scatter")
plt.scatter(students,marks)
plt.show()
plt.title("bar")
plt.bar(students,marks)
plt.show()