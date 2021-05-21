# Date 13-05-2021
import time as module
import numpy as np

# mo = input("Enter module name")
# print((dir(pandas)))
# print(dir(pandas.BooleanDtype))
total_length_of_module_all_functions = len(dir(module))-1
# print(total_length_of_module_all_functions)
module_name = str(module).split("'")[1]

list_of_module_all_functions_and_sub_functions = np.array(module_name)
print(dir(module)[total_length_of_module_all_functions])

while True:
    total_length_of_module_all_functions -= 1
    sub_function_name = str(dir(module)[total_length_of_module_all_functions])
    print(sub_function_name)
