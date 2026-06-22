import pandas as pd
employee_data = {
    "Employee ID": [101, 102, 103, 104, 105],
    "Name": ["Anna Smith", "John Doe", "Bilal Khan", "Diaz Cruz", "Mary Jones"],
    "Department": ["Sales", "Marketing", "Engineering", "HR", "Engineering"],
    "Salary": [65000, 55000, 95000, 48000, 105000],
    "Marks": [92, 78, 85, 60, 95],
    "Age": [28, 34, 41, 23, 38]
}
var=pd.DataFrame(employee_data)
print(var)
print(var.sort_values("Salary", ascending=False))
print(var.sort_values("Marks", ascending=True))
print(var.sort_values("Age", ascending=True))