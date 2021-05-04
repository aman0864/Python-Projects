# Date 11-4-2021
# Import string and random module
import random
import time

# Randomly generate a ascii value
# from 'A' to 'Z'


in1 = input("Entre the starting alphabet\n")
in2 = input("Entre the ending alphabet\n")


while(True):
    try:
        if (in1 > in2):
            in1, in2 = in2, in1
        randomUpperLetter = chr(random.randint(ord(in1), ord(in2))).upper()
        # print(randomUpperLetter)

    except:
        print(
            "\n\nPlease enter only one Alphabet.\nFor ex.---> A, B, C, .........., X, Y, Z")
    try:
        print("What's the numeric value of", randomUpperLetter)
        initial_time = time.time()
        in3 = int(input())+96
        time_taken_by_you = time.time()-initial_time
        ascii = chr(in3).upper()
        # print(ascii)
        if (ascii == randomUpperLetter):
            print(
                f"Congratulations! {randomUpperLetter} belongs to {in3-96} place.\nYou had taken {time_taken_by_you} seconds to tell the answer.\n\n")
        elif (ascii != randomUpperLetter):
            in4 = ord(randomUpperLetter)
            print(
                f"Sorry! You need to practice more.\n{randomUpperLetter} belongs to {in4-64} place; but you entered {in3-96}.\nYou had taken {time_taken_by_you} seconds to tell us the wrong answer.\n\n")
            
    except:
        print("Please enter numbers between 1-26")
        
