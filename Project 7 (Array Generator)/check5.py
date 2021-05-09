import numpy as np
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 45, 7])
# Convert 1D array to a 2D numpy array of 2 rows and 3 columns
arr_2d = np.reshape(arr, (3, 4))
print(arr)
print(arr_2d)
