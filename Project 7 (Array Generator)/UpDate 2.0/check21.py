from random import randint as rdi
# from random import uniform as uni


def random_value_generator(minimum_number_function, maximum_number_function, minimum_value_after_decimal_function=0, maximum_value_after_decimal_function=0):
    if minimum_value_after_decimal_function == 0 and maximum_value_after_decimal_function == 0:
        return rdi(minimum_number_function, maximum_number_function)
    else:
        random_float_value_user_need = str(rdi(minimum_number_function, maximum_number_function))+'.'+str(
            rdi(minimum_value_after_decimal_function, maximum_value_after_decimal_function))
        return float(random_float_value_user_need)


a1 = random_value_generator(214, 8778, 2, 15)
print(a1)
