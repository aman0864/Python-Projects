# Date 18-04-2021
# the below program can take screenshot and can extract text from that screenshot

import time
import pyautogui
import os
from PIL import Image
import cv2
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

time.sleep(4)

im1 = pyautogui.screenshot()
im1.save("im1.png")
img = cv2.imread("im1.png", 0)
height, width = img.shape[:2]
start_row, start_col = int(height*.70), int(width*.32)
end_row, end_col = int(height*.85), int(width*.95)
cropped = img[start_row:end_row, start_col-50:end_col+50]
# cv2.imshow("Cropped Image", cropped)
# cv2.waitKey(0)
cropped = cropped
# cropped = cv2.line(cropped, (1080, 120), (55445, 0), (0, 0, 0), 50)
# cv2.imshow("Cropped Image", cropped)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
img = Image.open("im1.png")
chat_text = tess.image_to_string(img)
os.remove("im1.png")

print(chat_text)
