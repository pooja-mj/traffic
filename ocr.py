import cv2
import pytesseract
from PIL import Image

global lp_str
lp_str = pytesseract.image_to_string(Image.open('lp.png'))
