import pytesseract
from PIL import Image
import os

tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image_path = r'C:\Wasteless\uploads\test.png'

print("1. Starting script...")

if not os.path.exists(tesseract_path):
    print(f"2. ERROR: Tesseract not found at {tesseract_path}")
else:
    print("2. Tesseract executable found.")

if not os.path.exists(image_path):
    print(f"3. ERROR: Image not found at {image_path}")
else:
    print("3. Image found.")

try:
    print("4. Attempting to run OCR...")
    pytesseract.pytesseract.tesseract_cmd = tesseract_path
    text = pytesseract.image_to_string(Image.open(image_path))
    print(f"5. OCR Result: {text}")
except Exception as e:
    print(f"5. ERROR: {str(e)}")

print("6. Finished.")