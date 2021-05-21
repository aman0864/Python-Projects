# Date 13-05-2021
import random as module
import numpy as np


total_length_of_module_all_functions = len(dir(module))-1
total_length_of_module_all_functions_max_please_do_not_change = len(
    dir(module))
total_length_of_module_all_functions_max = len(dir(module))
# print(total_length_of_module_all_functions)
module_name = str(module).split("'")[1]

list_of_module_all_functions_and_sub_functions = np.array([module_name])


while total_length_of_module_all_functions >= 0:
    total_length_of_module_all_functions -= 1
    sub_function_name = str(dir(module)[total_length_of_module_all_functions])
    # print(sub_function_name)
    # list_of_module_all_functions_and_sub_functions = np.append(
    #     list_of_module_all_functions_and_sub_functions, '\n\n\n\n\n\u203A\u203A\u203A\u203A\u203A\u203A\u203A\u203A' + sub_function_name)
    print(sub_function_name)
    print(sub_function_name.__doc__)
