import numpy as np

# creating an array
arr = np.array([1], dtype="int32")
print('Original Array : ', arr)

print(arr.dtype)
# arr = arr.astype = "float64"
arr = arr.astype(np.float64)
print(arr.dtype)
# appending to the array
# arr = np.append(arr, [7])
# print('Array after appending : ', repr(arr))
