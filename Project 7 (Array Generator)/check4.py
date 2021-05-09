import numpy as np
ary2d = np.array([[21, 43, 61, 21, 2], [324, 12, 5, 2, 1],
                  [1, 3, 6, 24, 27], [34, 2, 332, 12, 41]])
print(ary2d)
print(5*'\n')
ary2d = np.append(ary2d, 21, [0, 5])
# append(​arr, values, axis​)
# append(​arr, values, axis​)
print(ary2d)
