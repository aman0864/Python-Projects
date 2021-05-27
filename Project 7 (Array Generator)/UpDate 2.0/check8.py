from random import randint as rdi
from random import uniform as uni
import numpy as np

# creating an array
arr = np.array([rdi(0, 2002)], dtype="int32")
print('Original Array : ', arr)

print(arr.dtype)
# arr = arr.astype = "float64"
arr = arr.astype(np.float64)
print(arr.dtype)
# appending to the array
# arr = np.append(arr, [7])
# print('Array after appending : ', repr(arr))
# random.uniform(1.5, 1.9)
# creating an array
arr = np.array([uni(0, 2002)], dtype="float32")
print('Original Array : ', arr)

print(arr.dtype)
# arr = arr.astype = "float64"
arr = arr.astype(np.float64)
print(arr.dtype)
# appending to the array
# arr = np.append(arr, [7])
# print('Array after appending : ', repr(arr))
# random.uniform(1.5, 1.9)
