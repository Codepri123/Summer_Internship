import matplotlib.pyplot as plt

students = ["A", "B", "C", "D", "E"]
marks = [78, 85, 90, 66, 88]
attendance = [90, 85, 95, 80, 92]

plt.figure(figsize=(6, 6))  # Decrease overall graph size

plt.subplot(2, 2, 1)
plt.title("Line Plot")
plt.plot(students, marks ,marker="o")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.grid()
plt.subplot(2, 2, 2)
plt.title("Bar Plot")
plt.bar(students, attendance)
plt.xlabel("Students")
plt.ylabel("Attendance")

plt.subplot(2, 2, 3)
plt.title("Scatter Plot")
plt.scatter(students, marks)
plt.xlabel("Students")
plt.ylabel("Marks")
plt.grid()
plt.subplot(2, 2, 4)
plt.title("Pie Plot")
plt.pie(marks, labels=students)
plt.grid()

plt.tight_layout()
plt.show()