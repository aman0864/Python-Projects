# Date 18-04-2021
import pyautogui
import time

type_your_message_here = "Nothing"
how_many_times_you_need_to_print_your_message = 500000000

time.sleep(5)
for i in range(0, how_many_times_you_need_to_print_your_message):
    pyautogui.write(type_your_message_here, interval="0")
    pyautogui.press("enter")
    how_many_times_you_need_to_print_your_message -= 1
