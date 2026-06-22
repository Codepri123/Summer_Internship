# Challenge 3: Flattening the Matrix (Reshaping) [1]
# Goal: Turn a 2D grid back into a single, flat line of data.
# Tasks:
# Copy this 2D array:
# Use the .flatten() method to convert it into a 1D array.
# Print the flat array. It should look like: [1 2 3 4]
import numpy as np
grid = np.array([[1, 2],[1,5], [3, 4]])
print(grid.reshape(-1))
print(grid.flatten())