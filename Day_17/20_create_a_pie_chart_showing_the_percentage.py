import matplotlib.pyplot as plt
students={
"Food" : 300,
"Rent" : 500,
"Travel" : 150,
"Shopping" : 250
}

plt.pie(students.values(),labels=students.keys())
plt.show()