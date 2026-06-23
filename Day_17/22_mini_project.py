import matplotlib.pyplot as plt
students = ["A","B","C","D","E"]
marks = [78,85,90,66,88]
attendance = [90,85,95,80,92]
plt.subplot(2,2,1)
plt.title("Line plot")
plt.plot(students,marks)
plt.subplot(2,2,2)
plt.title("bar plot")
plt.bar(students,attendance)
plt.subplot(2,2,3)
plt.title("scatter plot")
plt.scatter(students,marks)
plt.subplot(2,2,4)
plt.title("pie plot")
plt.pie(marks,labels=students)
plt.show()