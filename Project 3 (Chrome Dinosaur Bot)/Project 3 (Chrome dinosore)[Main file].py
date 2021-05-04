# Date 16-04-2021

import pyautogui
import time
# from numpy import asarray
from PIL import Image, ImageGrab


def hit(key):
    pyautogui.keyDown(key)
           

def obsticle_in_front_or_not(data):      
    for i in range(500, 660):
        for j in range(500, 678):                                     
            if data[i, j] < 100:
                return True                      
    return False 
  

if __name__ == "__main__":
    print("Hey! Dino bot is just starting in 4 seconds")
    time.sleep(4)
    hit("space") 
    while True: 
        image = ImageGrab.grab().convert("L")  
        data = image.load()
        if obsticle_in_front_or_not(data):
            hit("space")
 





