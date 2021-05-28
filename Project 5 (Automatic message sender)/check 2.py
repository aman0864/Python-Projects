# Date 18-04-2021
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
from PIL import Image

img = Image.open("ocr1.png")
print(tess.image_to_string(img))
