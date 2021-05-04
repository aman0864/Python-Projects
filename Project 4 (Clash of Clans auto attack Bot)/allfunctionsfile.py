import pyautogui
import time

def key_board_key(key_name):
    pyautogui.keyDown(key_name)
    time.sleep(0.1)
    pyautogui.keyUp(key_name)

def move_and_click(x, y):
    pyautogui.moveTo(x, y)
    time.sleep(0.03)
    pyautogui.click(button="left")


def open_coc():
    move_and_click(973, 1079)
    move_and_click(760, 1063)


def click_on_attack_menu():
    move_and_click(1022, 1016)
    time.sleep(0.3)
    move_and_click(1086, 816)

def look_for_base_by_scrolling(no_of_times_you_need_to_scroll):
    no_of_times_scroll_is_done = int(0)
    for no_of_times_scroll_is_done in range(no_of_times_you_need_to_scroll):
        pyautogui.moveTo(1301, 657)
        time.sleep(0.05)
        pyautogui.mouseDown(button="left")
        pyautogui.moveTo(x=1301, y=1003)
        pyautogui.mouseUp(button="left")
    time.sleep(0.5)

def final_click_on_attack():
    move_and_click(1389,861)
    time.sleep(0.02)
    move_and_click(1389,861)
    time.sleep(4)

def deployeing_heros():
    key_board_key("3")
    move_and_click(1511, 828)
    key_board_key("3")
    time.sleep(2.4)

def returning_home_base():
    key_board_key("E")
    time.sleep(0.2)
    key_board_key("O")
    time.sleep(0.2)
    key_board_key("5")
    time.sleep(4.2)

    
