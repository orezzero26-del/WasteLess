"""Create a test image with an expiry date"""
from PIL import Image, ImageDraw, ImageFont

# Create white image
img = Image.new('RGB', (600, 200), color='white')
draw = ImageDraw.Draw(img)

# Add text that looks like a product label
draw.text((50, 30), "PRODUCT: MILK", fill='black')
draw.text((50, 70), "Best before: 2025/12/25", fill='black')
draw.text((50, 110), "Store in cool dry place", fill='black')
draw.text((50, 150), "EXP: 2025/12/25", fill='black')

# Save
img.save('test_image.jpg')
print("Test image created: test_image.jpg")
print("Run: python ocr_reader.py test_image.jpg")