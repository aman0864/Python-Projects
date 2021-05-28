# Date 18-04-2021
import pyautogui
import time

time.sleep(5)


def values(n_value):
    x = f"B_i_n_a_r_y  value of {n_value} is -->{bin(n_value)}"
    pyautogui.write(x, interval="0")
    pyautogui.press("enter")
    x = f"Octa Decimal value of {n_value} is -->{oct(n_value)}"
    pyautogui.write(x, interval="0")
    pyautogui.press("enter")
    x = f"Hexa Decimal value of {n_value} is -->{hex(n_value)}"
    pyautogui.write(x, interval="0")
    pyautogui.press("enter")


def printing(n):
    while True:
        values(n)
        n -= 1
