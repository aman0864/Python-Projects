# Date 26-04-2021
from datetime import datetime
from time import sleep

#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it
#! Failed to do it


def dtd():
    """dtd = date time day
       dtdv = date time day variable
    """

    dtdv = "On", str(datetime.now())[:10], str(
        datetime.today().strftime("%A")),
    "completed at"+str(datetime.now())[10:19]
    return dtdv


# dtd()
# print(dtdv)

def choice():
    ch = input("Which Subject do you need to deal with!\n").upper()
    if ch == "PHYSICS" or ch == "CHEMISTRY" or ch == "BIOLOGY" or ch == "MATHS" or ch == "MAT" or ch == "MENTAL ABILITY" or ch == "ENGLISH TEXT" or ch == "ENGLISH GR" or ch == "ENGLISH GRAMMAR" or ch == "GEOGRAPHY" or ch == "HISTORY" or ch == "CIVICS" or ch == "ECONOMICS":
        return ch

    else:
        print("Please select only avaliable Subjects!\nAnd, re-start the program.")
        sleep(5)
        exit()


# def opening_a_file(file_name, category):
#     try:
#         with open(file_name, category):


# print(choice())
if choice() == "PHYSICS":
    chc = int(input("\n\nPlease select the chapter from the given list.\nType 1 for Chapter 10 i.e. Light – Reflection and Refraction.\nType 2 for Chapter 12 i.e. Electricity.\nType 3 for Chapter 13 i.e. Magnetic Effects of Electric Current.\nType 4 for Chapter 14 i.e. Sources of Energy.\n"))
    # chfs means choice for subjects i.e. what you want to do with the particular subject which is selected by you.
    # todo chfs = input(
    # todo     f"What you want to do with PHYSICS i.e. check your previous progress or add a new progress.\nType PREVIOUS or P to previous progress\nType ADD or A to add a new progress.").upper()
    # chc stands for choice for the chapter
    # print(chfs)
    if chc == 1:
        chfs = input(f"What you want to do i.e. check your previous progress or add a new progress.\nType PREVIOUS or P to check your previous progress\nType ADD or A to add a new progress.").upper()
        if chfs == "PREVIOUS" or chfs == "P":
            try:
                with open("physics-ch1.txt", "r") as file1:
                    print(file1.read())
            except:
                print("No such file found please enter data to it first!")
                sleep(5)
                exit()
        elif chfs == "A" or chfs == "ADD":
            try:
                with open("physics-ch1.txt", "a") as file1:
                    file1.write(
                        input("Please tell us the time you taked to revise/learn it!") +
                        "On " + str(datetime.now())[:10] + " "+str()
                        except:
                        with open("physics-ch1.txt", "w") as file1:
                        file1.write(
                            input("Please tell us the time you taked to revise/learn it!") + datetime.today().strftime("%A")) + " completed at"+str(datetime.now())[10:19])
