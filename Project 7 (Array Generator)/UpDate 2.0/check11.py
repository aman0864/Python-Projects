import sys
import numpy as np
pynumpy = np.arange(20)
print(pynumpy)
with open('Array Example.txt', 'r') as f1:
    r = f1.read()
print(r)
print(sys.getsizeof(r))

# b = sys.getsizeof('geeks')
# print(b)

# c = sys.getsizeof(('g', 'e', 'e', 'k', 's'))
# print(c)

# d = sys.getsizeof(['g', 'e', 'e', 'k', 's'])
# print(d)

# e = sys.getsizeof({1, 2, 3, 4})
# print(e)

# f = sys.getsizeof({1: 'a', 2: 'b', 3: 'c', 4: 'd'})
# print(f)
