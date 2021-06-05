import os

location_of_file = str(os.path.dirname(
    os.path.realpath(__file__)))+"\product_list"


with open(location_of_file, 'r')as file:
    data_to_read = file.read()
    data_to_read = data_to_read.split('$')
    del data_to_read[len(data_to_read)-1]
    data_to_read = ' '.join([str(elem) for elem in data_to_read])
    data_to_read = data_to_read.replace(' ', '|')
    data_to_read = data_to_read.split('|')
    if '5458' in data_to_read:
        print('pass')
