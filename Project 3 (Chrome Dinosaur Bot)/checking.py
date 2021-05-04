


 # Date 16-04-2021

import pyautogui
import time
# from numpy import asarray
from PIL import Image, ImageGrab

def hit(key):
    pyautogui.keyDown(key)


# def take_a_screenshot():
    
#     return image


if __name__ == "__main__":
    time.sleep(1)
    
    image = ImageGrab.grab().convert("L")
    data = image.load()
    # print(asarray(image))
    for i in range(500, 660):
        for j in range(500, 678):
            data[i,j]=0


    image.show()
