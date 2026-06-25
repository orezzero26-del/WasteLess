import pytesseract
from PIL import Image, ImageEnhance, ImageOps

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    try:
        img = Image.open(image_path)
        
        # تحسين الصورة لتسهيل القراءة
        img = ImageOps.grayscale(img)
        img = ImageEnhance.Contrast(img).enhance(2)
        
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        return str(e)