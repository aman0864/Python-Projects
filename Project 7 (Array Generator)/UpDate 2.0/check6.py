import numpy as np

# creating an array
arr = np.array([1], dtype="int64")
print('Original Array : ', arr)

# appending to the array
arr = np.append(arr, [7])
print('Array after appending : ', repr(arr))
