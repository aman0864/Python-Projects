from random import randint as rdi
from random import uniform as uni
import numpy as np
try:
    float_or_integer = int(input(
        'Please tell us that you need a float or an integer.\nEntre 1 for Float.\nEntre 2 for Integer.\n'))
    if float_or_integer != 1 or float_or_integer != 2:
        print(2, 5*"\n")

except:
    print(2, 5*"\n")
try:
    minimum_number = int(
        input('Please enter the minimum value of number in your Array\n'))
    maximum_number = int(
        input('Please enter the maximum value of number in your Array\n'))
except:
    print(error_msg_1, 5*"\n")
    if minimum_number > maximum_number:
        minimum_number, maximum_number = maximum_number, minimum_number

#! Now the input comming is done and the time starts for outupt and processing
#! Now the input comming is done and the time starts for outupt and processing
#! Now the input comming is done and the time starts for outupt and processing
#! Now the input comming is done and the time starts for outupt and processing
#! Now the input comming is done and the time starts for outupt and processing
process1_multiplaction_of_rows_and_columns_variable_to_get_outuput_array = 10
if float_or_integer == 1:
    outuput_array = np.append([uni(minimum_number, maximum_number)])
    process1_multiplaction_of_rows_and_columns_variable_to_get_outuput_array -= 1
elif float_or_integer == 2:
    outuput_array = np.append([rdi(minimum_number, maximum_number)])
    process1_multiplaction_of_rows_and_columns_variable_to_get_outuput_array -= 1
print(outuput_array)
