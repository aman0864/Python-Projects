# Date 27-05-2021
from random import randint as rdi
from random import uniform as uni
from time import sleep as sl
from time import time as dt
from pyperclip import copy as co
import numpy as np
import sys
import os


def random_value_generator(minimum_number_function, maximum_number_function, minimum_value_after_decimal_function=0, maximum_value_after_decimal_function=0):
    if minimum_value_after_decimal_function == 0 and maximum_value_after_decimal_function == 0:
        return rdi(minimum_number_function, maximum_number_function)
    else:
        random_float_value_user_need = str(rdi(minimum_number_function, maximum_number_function))+'.'+str(
            rdi(minimum_value_after_decimal_function, maximum_value_after_decimal_function))
        return float(random_float_value_user_need)


error_msg_1 = 'Please Enter only Numeric values!'
error_msg_2 = 'Please select a valid option'
columns = 1
z_axis = 1
truely_random_or_not = None
minimum_digits_after_decimal = 0
maximum_digits_after_decimal = 0

# rd.randint(0, 22)
while True:
    try:
        choice = int(input(
            f'Please tell us that what type of Array you are willing to generate!\nEnter 1 to generate a 1 Dimensional Array.\nEnter 2 to generate a 2 Dimensional Array.\nEnter 3 to generate a 3 Dimensional Array.\n'))
    except:
        print(error_msg_2, 5*"\n")
        sl(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        continue
    if choice == 1:
        try:
            rows = int(
                input('Now please tell that how many columns you need to generate\n'))
        except:
            print(error_msg_1, 5*"\n")
            sl(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
    elif choice == 2:
        try:
            rows = int(
                input('Now please tell that how many rows and columns you need to generate\nFirst tell us about Rows.\n'))
            columns = int(input('Now tell us about Columns.\n'))
        except:
            print(error_msg_1, 5*"\n")
            sl(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
    elif choice == 3:
        try:
            rows = int(
                input('Now please tell that how many rows and columns you need to generate\nFirst tell us about Rows.\n'))
            columns = int(input('Now tell us about Columns.\n'))
            z_axis = int(
                input('Now tell us about how many Z axis you need to generate.\n'))
        except:
            print(error_msg_1, 5*"\n")
            sl(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
    else:
        print(error_msg_2, 5*"\n")
        sl(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        continue
    try:
        minimum_number = float(
            input('Please enter the minimum value of number in your Array\n'))
        maximum_number = float(
            input('Please enter the maximum value of number in your Array\n'))
    except:
        print(error_msg_1, 5*"\n")
        sl(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        continue
    if minimum_number > maximum_number:
        minimum_number, maximum_number = maximum_number, minimum_number

    try:
        float_or_integer = int(input(
            'Please tell us that you need a float or an integer.\nEntre 1 for Float.\nEntre 2 for Integer.\n'))
        if float_or_integer != 1 and float_or_integer != 2:
            print(error_msg_2, 5*"\n")
            sl(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue

    except:
        print(error_msg_1, 5*"\n")
        sl(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        continue

    if float_or_integer == 1:
        try:
            truely_random_or_not = input(
                'If need a truely random Float values in your Array Press T.\nOr if need a to Costumize random Float values in your Array Press C.\n').lower()

            if truely_random_or_not != 'c' and truely_random_or_not != 't':
                print(error_msg_2, 5*"\n")
                sl(3)
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
            if truely_random_or_not == 'c':
                minimum_digits_after_decimal = int(
                    input('Please enter the minimum value you need to get after decimal in your Array.\n'))
                maximum_digits_after_decimal = int(
                    input('Please enter the maximum value you need to get after decimal in your Array.\n'))
                if minimum_digits_after_decimal <= -1:
                    minimum_digits_after_decimal = 0
                if maximum_digits_after_decimal <= -1:
                    maximum_digits_after_decimal = 0
                if minimum_digits_after_decimal > maximum_digits_after_decimal:
                    minimum_digits_after_decimal, maximum_digits_after_decimal = maximum_digits_after_decimal, minimum_digits_after_decimal
        except:
            print(error_msg_1, 5*"\n")
            sl(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
    #! Now the input comming is done and the time starts for outupt and processing
    #! Now the input comming is done and the time starts for outupt and processing
    #! Now the input comming is done and the time starts for outupt and processing
    #! Now the input comming is done and the time starts for outupt and processing
    #! Now the input comming is done and the time starts for outupt and processing
    time_when_started = float(dt())
    process1_multiplaction_of_rows_and_columns_variable_to_get_outuput_array = rows*columns*z_axis
    if truely_random_or_not == 't':
        outuput_array = np.array([uni(minimum_number, maximum_number)])
    else:
        outuput_array = np.array(
            [random_value_generator(minimum_number, maximum_number, minimum_digits_after_decimal, maximum_digits_after_decimal)])
    process1_multiplaction_of_rows_and_columns_variable_to_get_outuput_array -= 1

    while(process1_multiplaction_of_rows_and_columns_variable_to_get_outuput_array != 0):
        if truely_random_or_not == 't':
            outuput_array = np.append(
                outuput_array, uni(minimum_number, maximum_number))
        else:
            outuput_array = np.append(
                outuput_array, random_value_generator(minimum_number, maximum_number, minimum_digits_after_decimal, maximum_digits_after_decimal))
        process1_multiplaction_of_rows_and_columns_variable_to_get_outuput_array -= 1
    if choice == 2:
        outuput_array = np.resize(outuput_array, (rows, columns))
    if choice == 3:
        outuput_array = np.resize(outuput_array, (z_axis, rows, columns))
    np.set_printoptions(threshold=sys.maxsize)

    print('Your array generated Sucessfuly\nYour array is generated in', float(dt())-float(time_when_started),
          'Seconds using Numpy!\n')
    if int(sys.getsizeof(outuput_array)) > 2000000:
        try:
            choice_2 = int(
                input('Please tell that what you want to do with generated array!\nEnter 1 to Copy to Clipboard. \nEnter 2 to store it in a file.\n'))
        except:
            print(error_msg_1, 5*"\n")
            sl(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        if choice_2 == 1:
            outuput_array_to_paste_on_clipboard = repr(outuput_array)
            co(f"{outuput_array_to_paste_on_clipboard}")
            print(repr(outuput_array))
            print('\nThe type of this array is', outuput_array.dtype)
            print(10*"\n")
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        elif choice_2 == 2:
            user_filename = str(input(
                'What name you need to give to your file(your file will be created with .txt extension)\n'))
            user_file_location_with_file_name = str(os.getcwd())+'\Files\ ' + \
                user_filename + '.txt'
            with open(user_file_location_with_file_name, "w") as file1:
                file1.write(str(repr(outuput_array)))
            print('Your Data is saved sucessfully in a file name \"' +
                  user_filename+'\" with extension .txt on the location\n'+user_file_location_with_file_name)
            print(10*"\n")
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        else:
            print(error_msg_2, 5*"\n")
            sl(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue

    else:
        outuput_array_to_paste_on_clipboard = repr(outuput_array)
        co(f"{outuput_array_to_paste_on_clipboard}")
        print(repr(outuput_array))
        print('\nThe type of this array is', outuput_array.dtype)
        print(10*'\nYour array is copied on clipboard!')
        print(10*"\n")
        print('Your array generated Sucessfuly\nYour array is generated in', float(dt())-float(time_when_started),
              'Seconds using Numpy!\n')
        continue
