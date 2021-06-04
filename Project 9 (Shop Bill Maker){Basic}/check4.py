import os
location_of_file = str(os.path.dirname(
    os.path.realpath(__file__)))+"\product_list"


with open(location_of_file, 'r')as file:
    data_to_read = file.read()
    data_to_read = data_to_read.split('$')
    del data_to_read[len(data_to_read)-1]


# data_to_read[0] = str(data_to_read).split('|')
# for i in data_to_read:
#     print(i)

print(data_to_read)
# data_to_read_0 = str(data_to_read[0]).split('|')
# print(data_to_read_0)
