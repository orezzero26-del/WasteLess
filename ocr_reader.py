"""
OCR Reader - Reads expiration dates from product images
"""

import re
from datetime import datetime
from PIL import Image, ImageEnhance
import pytesseract

# Set Tesseract path - CHANGE THIS to your installation path!
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def read_text_from_image(image_path):
    """Extract all text from an image"""
    try:
        img = Image.open(image_path)
        
        # Convert to grayscale for better OCR
        img = img.convert('L')
        
        # Increase contrast
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(2.0)
        
        # Extract text
        text = pytesseract.image_to_string(img)
        
        return text.strip()
    except Exception as e:
        print(f"Error reading image: {e}")
        return ""


def find_date_in_text(text):
    """Find expiration date in text"""
    # Look for date patterns
    patterns = [
        r'\d{4}[/\-\.]\d{2}[/\-\.]\d{2}',  # 2025/06/15
        r'\d{2}[/\-\.]\d{2}[/\-\.]\d{4}',  # 15/06/2025
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            date_str = match.group(0)
            # Try to parse the date
            for fmt in ['%Y/%m/%d', '%Y-%m-%d', '%Y.%m.%d', '%d/%m/%Y', '%d-%m-%Y']:
                try:
                    parsed = datetime.strptime(date_str, fmt)
                    return parsed.strftime('%Y-%m-%d')
                except:
                    continue
    
    return None


def process_product_image(image_path):
    """
    Process a product image and extract expiry date
    
    Returns:
        dict with extracted text and date
    """
    text = read_text_from_image(image_path)
    date = find_date_in_text(text)
    
    return {
        'text': text,
        'expiry_date': date,
        'success': date is not None
    }


# Test function
if __name__ == "__main__":
    # Test with command line argument
    import sys
    
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
        print(f"Processing: {image_path}")
        result = process_product_image(image_path)
        print(f"Extracted text: {result['text']}")
        print(f"Expiry date: {result['expiry_date']}")
    else:
        print("Usage: python ocr_reader.py <image_path>")