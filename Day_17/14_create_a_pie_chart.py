import matplotlib.pyplot as plt
import pandas as pd

students = {
    "programming": ["java", "python", "c++"],
    "marks": [40, 10, 25]
}

var = pd.DataFrame(students)

plt.pie(
    var["marks"],
    labels=var["programming"],
    colors=["red","orange","yellow"],
    explode=[0.1,0,0],
    shadow=[True]
)

plt.title("Programming Language Distribution")
plt.show()