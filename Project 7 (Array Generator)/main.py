from random import randint as rdi
from random import uniform as uni
from time import sleep as sl
from pyperclip import copy as co
import numpy as np

error_msg_1 = 'Please Enter only Numeric values!'
error_msg_2 = 'Please select a valid option'
columns = 1


# todo# def error_control_1(variable_name_where_to_store_data, statement_to_be_print, error_message_to_be_print):
# todo#     global choice
# todo#     choice = 1
# todo#     try:
# todo#         variable_name_where_to_store_data = int(
# todo#             input(statement_to_be_print))
# todo#     except:
# todo#         print(error_message_to_be_print)
# todo#         sl(10)
# todo#         exit()


# rd.randint(0, 22)
while True:
    try:
        choice = int(input(
            f'Please tell us that what type of Array you are willing to generate!\nPress 1 to generate a 1 Dimensional Array.\nPress 2 to generate a 2 Dimensional Array.\n'))
    except:
        print(error_msg_2, 5*"\n")
        sl(3)
        continue
    if choice == 1:
        try:
            rows = int(
                input('Now please tell that how many columns you need to generate\n'))
        except:
            print(error_msg_1, 5*"\n")
            sl(3)
            continue
    elif choice == 2:
        try:
            rows = int(
                input('Now please tell that how many rows and columns you need to generate\nFirst tell us about Rows.\n'))
            columns = int(input('Now tell us about Columns.\n'))
        except:
            print(error_msg_1, 5*"\n")
            sl(3)
            continue
    else:
        print(error_msg_2, 5*"\n")
        sl(3)
        continue
    try:
        minimum_number = int(
            input('Please enter the minimum value of number in your Array\n'))
        maximum_number = int(
            input('Please enter the maximum value of number in your Array\n'))
    except:
        print(error_msg_1, 5*"\n")
        sl(3)
        continue
    if minimum_number > maximum_number:
        minimum_number, maximum_number = maximum_number, minimum_number

    try:
        float_or_integer = int(input(
            'Please tell us that you need a float or an integer.\nEntre 1 for Float.\nEntre 2 for Integer.\n'))
        if float_or_integer == 1 or float_or_integer == 2:
            useless_variable = 1
        else:
            print(error_msg_2, 5*"\n")
            sl(3)
            continue

    except:
        print(error_msg_1, 5*"\n")
        sl(3)
        continue

    #! Now the input comming is done and the time starts for outupt and processing
    #! Now the input comming is done and the time starts for outupt and processing
    #! Now the input comming is done and the time starts for outupt and processing
    #! Now the input comming is done and the time starts for outupt and processing
    #! Now the input comming is done and the time starts for outupt and processing
    process1_multiplaction_of_rows_and_columns_variable_to_get_outuput_array = rows*columns
    if float_or_integer == 1:
        outuput_array = np.array([uni(minimum_number, maximum_number)])
        process1_multiplaction_of_rows_and_columns_variable_to_get_outuput_array -= 1
    elif float_or_integer == 2:
        outuput_array = np.array([rdi(minimum_number, maximum_number)])
        process1_multiplaction_of_rows_and_columns_variable_to_get_outuput_array -= 1

    while(process1_multiplaction_of_rows_and_columns_variable_to_get_outuput_array != 0):
        if float_or_integer == 1:
            outuput_array = np.append(
                outuput_array, uni(minimum_number, maximum_number))
            process1_multiplaction_of_rows_and_columns_variable_to_get_outuput_array -= 1
        elif float_or_integer == 2:
            outuput_array = np.append(
                outuput_array, rdi(minimum_number, maximum_number))
            process1_multiplaction_of_rows_and_columns_variable_to_get_outuput_array -= 1

    if choice == 2:
        outuput_array = np.resize(outuput_array, (rows, columns))
    outuput_array_to_paste_on_clipboard = repr(outuput_array)
    co(f"{outuput_array_to_paste_on_clipboard}")
    print(repr(outuput_array))
    print(10*"\n")
