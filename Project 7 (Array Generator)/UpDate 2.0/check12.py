import names
import random as rd
import numpy as np
user_in = int(input('Please enter a digit\n'))
gen = input('Please enter a Gender i.e. Male or Female\n').lower()
ar1 = np.array([names.get_full_name(gender=gen)])
user_in -= 1
while user_in != 0:
    name = names.get_full_name(gender=gen)
    for name in ar1:
        name = names.get_full_name(gender=gen)
    ar1 = np.append(ar1, name)
    user_in -= 1
# print(repr(ar1))
rd.shuffle(ar1)
print(repr(ar1))
