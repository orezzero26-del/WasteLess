from PIL import Image, ImageDraw, ImageFont

# Create 192x192 icon
img = Image.new('RGB', (192, 192), color='#4CAF50')
draw = ImageDraw.Draw(img)
draw.ellipse([40, 40, 152, 152], fill='white')
draw.text((70, 70), '📱', font=ImageFont.load_default())
img.save('icon-192.png')

# Create 512x512 icon
img = Image.new('RGB', (512, 512), color='#4CAF50')
draw = ImageDraw.Draw(img)
draw.ellipse([100, 100, 412, 412], fill='white')
draw.text((180, 180), '📱', font=ImageFont.load_default())
img.save('icon-512.png')

print("Icons created!")