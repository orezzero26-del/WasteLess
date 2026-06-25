import subprocess
import os

tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image_path = r'C:\Wasteless\uploads\test.png'

print("--- Starting Direct Test ---")

if not os.path.exists(tesseract_path):
    print("Error: Tesseract path is wrong.")
elif not os.path.exists(image_path):
    print("Error: Image not found.")
else:
    print("Executing Tesseract command...")
    # هذا الأمر يقوم بتشغيل Tesseract مباشرة على الصورة
    result = subprocess.run([tesseract_path, image_path, "stdout"], capture_output=True, text=True, encoding='utf-8')
    print("Result Found:")
    print(result.stdout)
    if result.stderr:
        print("Error details:", result.stderr)
