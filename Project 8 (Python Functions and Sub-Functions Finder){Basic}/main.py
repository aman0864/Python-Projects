# Date 13-05-2021
import numpy as module
# import tensorflow as module
import numpy as np
from wikipedia import summary as sm
import os
from pyperclip import copy as co
import sys


total_length_of_module_all_functions = len(dir(module))-1
total_length_of_module_all_functions_max_please_do_not_change = len(
    dir(module))
total_length_of_module_all_functions_max = len(dir(module))
# print(total_length_of_module_all_functions)
module_name = str(module).split("'")[1]

one_dimensional_array_of_module_all_functions_and_there_meaning = np.array([])
one_dimensional_array_of_all_module_names = np.array([module_name])


while total_length_of_module_all_functions >= 0:
    sub_function_name = dir(module)[total_length_of_module_all_functions]
    # print(sub_function_name)
    one_dimensional_array_of_module_all_functions_and_there_meaning = np.append(
        one_dimensional_array_of_module_all_functions_and_there_meaning, '\u203A\u203A\u203A\u203A\u203A\u203A\u203A\u203A' + sub_function_name)
    one_dimensional_array_of_all_module_names = np.append(
        one_dimensional_array_of_all_module_names, '\u27F9  ' + sub_function_name)
    # sub_function_name = str(dir(module)[total_length_of_module_all_functions])
    # print(sub_function_name.__doc__)
    # docs = module.sub_function_name.__doc__
    # sub_function_name = str(module)+sub_function_name
    sub_function_wekipedia_summary = sub_function_name.replace('_', '')
    try:
        one_dimensional_array_of_module_all_functions_and_there_meaning = np.append(
            one_dimensional_array_of_module_all_functions_and_there_meaning, (sm(sub_function_wekipedia_summary)+'\n\u290A\n\u290A\n\u290B\n\u290B'))
    except:
        one_dimensional_array_of_module_all_functions_and_there_meaning = np.append(
            one_dimensional_array_of_module_all_functions_and_there_meaning, 'No data avaliable'+'\n\n\n\n\n')
    # one_dimensional_array_of_module_all_functions_and_there_meaning = np.append(
    #     one_dimensional_array_of_module_all_functions_and_there_meaning, sub_function_name.__doc__)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(str(total_length_of_module_all_functions_max_please_do_not_change-1)+' functions of ' +
          str(total_length_of_module_all_functions)+' are left.')

    total_length_of_module_all_functions -= 1
os.system('cls' if os.name == 'nt' else 'clear')
np.set_printoptions(threshold=sys.maxsize)
co(repr(one_dimensional_array_of_module_all_functions_and_there_meaning))
total_length_of_module_all_functions_max = 0
# print(repr(one_dimensional_array_of_module_all_functions_and_there_meaning))
while total_length_of_module_all_functions_max != (total_length_of_module_all_functions_max_please_do_not_change+1):
    print(
        one_dimensional_array_of_module_all_functions_and_there_meaning[total_length_of_module_all_functions_max])
    total_length_of_module_all_functions_max += 1

print('\n\n\n\n\n')
total_length_of_module_all_functions_max = 0
while total_length_of_module_all_functions_max != (total_length_of_module_all_functions_max_please_do_not_change+1):
    print(
        one_dimensional_array_of_all_module_names[total_length_of_module_all_functions_max])
    total_length_of_module_all_functions_max += 1
