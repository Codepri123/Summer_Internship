import pandas as pd
import numpy as np
employee_data = {
    "Employee ID": [101, 102, 103, 104, 105],
    "Name": ["Anna Smith", "John Doe", "Bilal Khan", "Diaz Cruz", "Mary Jones"],
    "Department": ["Sales", "Marketing", "Engineering", "HR", "Engineering"],
    "Salary": [65000, 55000, 95000, 48000, 105000],
    "Marks": [np.nan, 78, 85, np.nan, 95],
    "Age": [28, 34, 41, 23, 38]
}
var=pd.DataFrame(employee_data)
print(var)
print(var.duplicated("Marks"))
print(var.isnull())