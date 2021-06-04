# Date 04-06-2021
from time import sleep as sl
import os
import sys
from fpdf import FPDF
from itertools import chain as ch

pdf = FPDF()

location_of_file = str(os.path.dirname(
    os.path.realpath(__file__)))+"\product_list"

error_msg_1 = 'Please Enter only Numeric values!'
error_msg_2 = 'Please select a valid option'
pdf_name = str(os.path.dirname(
    os.path.realpath(__file__)))+'\my pdf'


def error_msg(msg):
    print(msg, 5*"\n")
    sl(3)
    os.system('cls' if os.name == 'nt' else 'clear')


def pdf_common_template():
    pdf.add_page()
    pdf.set_font('Arial', size=20)
    pdf.cell(200, 10, txt='Shop Name', ln=2, align='C')
    pdf.cell(100, 10, txt='________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________', ln=2, align='C')


def pdf_template_for_shopkeeper(li):
    pdf_common_template()
    pdf.cell(200, 10, txt='Name', ln=2, align='L')
    pdf.cell(200, -10, txt='Id', ln=2, align='C')
    pdf.cell(200, 10, txt='Price', ln=2, align='R')

    i_constant = len(li)
    i = 0
    # Maximum number 69
    how_many_time_loop_runs = 0
    while i < i_constant:

        pdf.cell(200, 10, txt=str(li[i]), ln=2, align='L')
        i += 1
        pdf.cell(200, -10, txt=str(li[i]), ln=2, align='C')
        i += 1
        pdf.cell(200, 10, txt=str(li[i]), ln=2, align='R')
        i += 1

        how_many_time_loop_runs += 1

        if how_many_time_loop_runs == 23:
            how_many_time_loop_runs = 0
            pdf_common_template()
            pdf.cell(200, 10, txt='Name', ln=2, align='L')
            pdf.cell(200, -10, txt='Id', ln=2, align='C')
            pdf.cell(200, 10, txt='Price', ln=2, align='R')
    # pdf.output(str(pdf_name)+'.pdf')


def pdf_template_for_buyer(li):

    pdf_common_template()

    pdf.cell(40, 10, txt='Name', ln=2, align='L')
    pdf.cell(80, -10, txt='Id', ln=2, align='R')
    pdf.cell(120, 10, txt='Price', ln=2, align='R')
    pdf.cell(160, -10, txt='Quantity', ln=2, align='R')
    pdf.cell(200, 10, txt='Tot', ln=2, align='R')

    i_constant = len(li)
    i = 0
    # Maximum number 69
    how_many_time_loop_runs = 0
    while i < i_constant:

        pdf.cell(40, 10, txt=str(li[i]), ln=2, align='L')
        i += 1
        pdf.cell(80, -10, txt=str(li[i]), ln=2, align='R')
        i += 1
        pdf.cell(120, 10, txt=str(li[i]), ln=2, align='R')
        i += 1
        pdf.cell(160, -10, txt=str(li[i]), ln=2, align='R')
        i += 1
        pdf.cell(200, 10, txt=str(li[i]), ln=2, align='R')
        i += 1

        how_many_time_loop_runs += 1

        if how_many_time_loop_runs == 22:
            how_many_time_loop_runs = 0
            pdf_common_template()
            pdf.cell(40, 10, txt='Name', ln=2, align='L')
            pdf.cell(80, -10, txt='Id', ln=2, align='R')
            pdf.cell(120, 10, txt='Price', ln=2, align='R')
            pdf.cell(160, -10, txt='Quantity', ln=2, align='R')
            pdf.cell(200, 10, txt='Tot', ln=2, align='R')

    # pdf.output(str(pdf_name)+'.pdf')


# print(help(pdf.html))
while True:
    user_choice_for_buyer = 'n'
    material_list_main = list('')

    try:
        user_choice = int(input(
            "Please tell what you want to do i.e.\nSell a product to a customer; Press 1 to do so.\nAdd product to your shop; Press 2 to do so.\nOr check the stock; Press 3 to do so.\n"))
        if (user_choice != 1 and user_choice != 2 and user_choice != 3):
            error_msg(error_msg_2)
            continue

    except:
        error_msg(error_msg_1)
        continue
    if user_choice == 1:
        while user_choice_for_buyer == 'n':
            try:
                user_choice_1_id = input(
                    "Press \'D\' to stop buying!\nPlease Enter the id of product!\n")
                if user_choice_1_id == 'd' or user_choice_1_id == 'D':
                    pdf_template_for_buyer(material_list_main)
                    pdf.output(str(pdf_name)+'.pdf')
                    exit()
                with open(location_of_file, 'r')as file:
                    data_to_read = file.read()
                    data_to_read = data_to_read.split('$')
                    del data_to_read[len(data_to_read)-1]
                    data_to_read = ' '.join([str(elem)
                                            for elem in data_to_read])
                    data_to_read = data_to_read.replace(' ', '|')
                    data_to_read = data_to_read.split('|')
                if str(user_choice_1_id) in data_to_read:
                    id_on_which_index = data_to_read.index(
                        str(user_choice_1_id))
                    material_list = data_to_read[id_on_which_index -
                                                 1:id_on_which_index+2]
                    quantity = input("Please Enter the Quantity.\n")
                    total = int(quantity)*int(material_list[2])
                    # print(total)
                    # print(material_list)
                    # print(type(material_list))
                    material_list.append(quantity)
                    material_list.append(total)
                    # print(material_list)
                    material_list_main.extend(material_list)
                    print(material_list_main)

            except:
                # print(e)
                error_msg(error_msg_1)
                exit()
                # continue

    elif user_choice == 2:
        try:
            product_name = input("Please Enter the name of the product!\n")
            product_id = int(input("Please Enter the id of the product!\n"))
            product_price = input(
                "Please Enter the price of the product!\n")
            product_to_add_in_file = product_name+'|' + \
                str(product_id) + '|'+product_price + '$'
            with open(location_of_file, 'a')as file:
                file.write(product_to_add_in_file)
        except:
            error_msg(error_msg_1)
            continue

    elif user_choice == 3:
        try:
            with open(location_of_file, 'r')as file:
                data_to_read = file.read()
                data_to_read = data_to_read.split('$')
                del data_to_read[len(data_to_read)-1]
                data_to_read = ' '.join([str(elem) for elem in data_to_read])
                data_to_read = data_to_read.replace(' ', '|')
                data_to_read = data_to_read.split('|')
        except Exception as e:
            error_msg(e)
            error_msg('File not Found!')
            continue
        try:
            user_choice_if_3 = int(input(
                "Please tell us that you need pdf or you can adjust in printing it on terminal.\nEnter 1 to make a pdf.\nEnter 2 to print it on a terminal.\n"))
        except:
            error_msg(error_msg_1)
        if user_choice_if_3 != 1 and user_choice_if_3 != 2:
            error_msg(error_msg_2)
            continue
        elif(user_choice_if_3 == 1):
            pdf_template_for_shopkeeper(data_to_read)
            # print(data_to_read)

    pdf.output(str(pdf_name)+'.pdf')
