# Date 13-05-2021
import time as module
import numpy as np

# mo = input("Enter module name")
# print((dir(pandas)))
# print(dir(pandas.BooleanDtype))
total_length_of_module_all_functions = len(dir(module))-1
module_name = str(module).split("'")[1]

list_of_module_all_functions_and_sub_functions = np.array([['module_name']])

while total_length_of_module_all_functions >= 0:
    total_length_of_module_sub_function = int(
        len(dir(dir(module)[total_length_of_module_all_functions])))
    module_function = dir(dir(module)[total_length_of_module_all_functions])
    module_function_to_show_on_list = f"\u27F9 {module_function}"
    list_of_module_all_functions_and_sub_functions = np.append(
        module_function_to_show_on_list, 0)
    total_length_of_module_all_functions -= 1
    while total_length_of_module_sub_function != -1:
        module_sub_function_to_show_on_list = f"\u00BB\u00BB\u00BB\u00BB\u00BB\u00BB\u00BB\u00BB\u00BB\u00BB {module_function}"
        list_of_module_all_functions_and_sub_functions = np.append(
            module_sub_function_to_show_on_list, 0)
        total_length_of_module_sub_function -= 1
    # module_all_functions_and_sub_functions_name =
print(list_of_module_all_functions_and_sub_functions)
