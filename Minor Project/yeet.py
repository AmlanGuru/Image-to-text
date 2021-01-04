import pyautogui
from PIL import Image
from pytesseract import *
pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img  = Image.open("text_to_convert.png")

output = pytesseract.image_to_string(img)

print(output)