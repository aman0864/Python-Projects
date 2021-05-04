# Date 29-3-2021

# This program is a part of Data Science in Python 3
# This program will help you to store the data of your customers who had buyed or taken loan from you


# with open("tutorial 31.txt") as file1:
#     print(file1.readlines())

import time


def gettime():
    """This function will help you to get date and time
    by using this syntax -
    file1.write("["+str(gettime())+"]: "+lock+"\n")
    """
    import datetime
    return datetime.datetime.now()


print("Welcome to our program!\n\n")


input1 = str(input(
    "Please enter the name of that person you need to see or add the data:\n")).title()
# print(input1)

# input2= str(input("Now tell us that what you want to do with his/her Data i.e. Edit or See.\nPress \"E\"to Edit and,\nPress \"S\"to See\n")).upper()

print("\nPress \"H\" for the old history of", input1, "\nPress \"A\" to add or deduct amount from",
      input1, "\n")
input2 = str(input()).upper()

# print(input2)

if (input2 != "H" and input2 != "A" and input2 != "T"):
    print("Please enter the input in the form only in \"H\" or \"A\"")
    useless = input("\n\n\n\n\nPress Enter to close!")


if (input2 == "H"):
    data1 = f"{input1}.txt"
    try:
        with open(data1, "r") as file1:
            print(file1.read())
            useless = input("\n\n\n\n\nPress Enter to close!")
    except:
        print(f"There is no data found for {input1}")
        useless = input("\n\n\n\n\nPress Enter to close!")


elif (input2 == "A"):
    data1 = f"{input1}.txt"
    with open(data1, "a") as file1:
        data2 = input("Tell us the reason\n")
        data3 = input(f"What's the amount given by you to {input1}\n")
        file1.write("\nTime----> [" + str(gettime()) + "]\nReason----> " +
                    str(data2)+"\nAmount----> " + str(data3) + "\n")
        # print(file1.read())

"""
elif (input2 == "T"):
    data1 = f"{input1}.[[total]].txt"
    with open(data1, "w") as file2:
        with open(data1, "r") as file1:
            var1=str(input(f"{input1} is taking money or giving money\nPress \"T\" if {input1} is Taking money\nPress \"G\" if {input1} is Giving money back\n")).upper()
            if (var1=="T" or var1=="G"):
                try:
                    if(var1=="T"): 
                        var2=int(input(f"How much money {input1} is Taking from you\n"))
                        file1=file1.read()
                        file2.write(file1+var2)
                    else:
                        # var1=="G" 
                        var2=int(input(f"How much money {input1} is Giving to you\n"))
                        file1=file1.read()
                        file2.write(file1-var2)
                except:
                    print("Please enter only integer value")
                    useless=input("Press enter to end the programe")
            else:
                print("Please enter the input in the form only in \"T\" or \"G\"")
                useless = input("\n\n\n\n\nPress Enter to close!")
    """

useless = input("\n\n\n\n\nPress Enter to close!")
