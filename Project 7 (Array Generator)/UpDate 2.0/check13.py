import names
import random as rd
import numpy as np
in1 = int(input('digits\n'))
gen = input('Gender\n')
if gen == '3':
    gen = int(gen)
else:
    gen = gen.lower()

gender_list = ['male', 'female']
if gen == 1:
    gen = 'male'
if gen == 2:
    gen = 'female'
if gen == 3 or 'any':
    gen = rd.choice(gender_list)
# print(dir(names))
# print(help(names.get_first_name))
# print(help(names.get_last_name))
first_name = names.get_first_name(gender=gen)
first_name_array = np.array([first_name])
last_name = str(names.get_last_name)
last_name_array = np.array([last_name])
while in1 != 0:
    if gen == 3 or 'any':
        gen = rd.choice(gender_list)
    first_name = str(names.get_first_name(gender=gen))
    for first_name in first_name_array:
        if gen == 3 or 'any':
            gen = rd.choice(gender_list)
        first_name = str(names.get_first_name(gender=gen))
    first_name_array = np.append(first_name_array, first_name)
    last_name = str(names.get_last_name)
    for last_name in last_name_array:
        last_name = str(names.get_last_name)
    last_name_array = np.append(last_name_array, last_name)
    in1 -= 1

rd.shuffle(first_name_array)
rd.shuffle(last_name_array)
print(repr(first_name_array))
print(repr(last_name_array))
