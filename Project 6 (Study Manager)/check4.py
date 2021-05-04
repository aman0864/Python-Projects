# Date 26-04-2021
from datetime import datetime
from time import sleep


def dtd():
    """dtd = date time day
       dtdv = date time day variable
    """

    global dtdv
    dtdv = "On", str(datetime.now())[:10], str(
        datetime.today().strftime("%A")),
    "completed at"+str(datetime.now())[10:19]
    # return dtdv
    print(dtdv)


# dtd()
# print(dtdv)
print("On " + str(datetime.now())[:10] + " "+str(
    datetime.today().strftime("%A")) + " completed at"+str(datetime.now())[10:19])
# print(dtdv)
