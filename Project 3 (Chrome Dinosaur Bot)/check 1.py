from PIL import ImageOps
import pyscreenshot as ImageGrab
import pyautogui
import time
import numpy as np

class Cordinates():
    
    # coordinates of replay button
    replay = (530, 516)
    # coordinates of top-right corner of dinosaur
    dino = (195, 522)

def restartGame():
    #au tomating the replay button
    pyautogui.click(Cordinates.replay)

def pressSpace():
    pyautogui.keyDown("space")
    # a small time sleep for space
    # to be easily recognized by the game
    time.sleep(0.05)
    print("Jump")
    pyautogui.keyUp("space")
restartGame()
time.sleep(1)
pressSpace()
def imgBox():
    box = (Cordinates.dino[0]+60, Cordinates.dino[1],
     Cordinates.dino[0]+160, Cordinates.dino[1]+20)
    image = ImageGrab.grab(box)

    grayImage = ImageOps.grayscale(image)

    a = np.array(grayImage.getcolors())

    print(a.sum())
    return(a.sum())
while True:
    imgBox()
def main():
    restartGame()
    while True:
        if(imgBox()!= 2247):
            pressSpace()
            time.sleep(0.1)

main()