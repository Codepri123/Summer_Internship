import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
var=pd.read_json("C:\\Users\\User\\Downloads\\student_submission_status.json")
print(var.head())
print(var.tail())
print(var.shape)