# Challenge 1: Matrix Statistics (Math)
# Goal: Find the highest, lowest, and total values in a dataset. [1]
# Tasks:
# Copy this matrix:
# Use a NumPy function to find and print the maximum value.
# Use a NumPy function to find and print the sum of all numbers.
import numpy as np
data = np.array([[10, 20, 30], [40, 50, 60]])
print(f"the highest value is :",data.max())
print(f"the total sum is :",data.sum())
print(f"the loweset value is :",data.min())