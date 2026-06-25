"""
Expiry Date Tracker & Recipe Suggester
Building AI Course Project
Features: Camera OCR, Manual Edit, Smart Alarms, Web Recipe Search
"""

import json
import os
import re
import webbrowser
from datetime import datetime, timedelta

# Try importing optional libraries
try:
    import cv2
    import pytesseract
    from PIL import Image
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    OCR_AVAILABLE = True
except:
    OCR_AVAILABLE = False
    print("⚠️  OCR not fully available. Install: pip install opencv-python pytesseract Pillow")
    print("   Also install Tesseract from: https://github.com/UB-Mannheim/tesseract/wiki")


class ProductDatabase:
    def __init__(self):
        self.filename = 'products.json'
        self.products = self.load()
    
    def load(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
    
    def save(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.products, f, indent=2, ensure_ascii=False)
    
    def add(self, name, expiry):
        product = {
            'name': name,
            'expiry': expiry,
            'added': datetime.now().strftime('%Y-%m-%d'),
            'alarms': {
                '7_days': (datetime.strptime(expiry, '%Y-%m-%d') - timedelta(days=7)).strftime('%Y-%m-%d'),
                '4_days': (datetime.strptime(expiry, '%Y-%m-%d') - timedelta(days=4)).strftime('%Y-%m-%d'),
                '2_days': (datetime.strptime(expiry, '%Y-%m-%d') - timedelta(days=2)).strftime('%Y-%m-%d'),
            }
        }
        self.products.append(product)
        self.save()
        return product
    
    def get_all(self):
        return sorted(self.products, key=lambda x: x['expiry'])
    
    def get_expiring(self, days=7):
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        result = []
        for p in self.products:
            expiry = datetime.strptime(p['expiry'], '%Y-%m-%d')
            left = (expiry - today).days
            if 0 <= left <= days:
                result.append({**p, 'days_left': left})
        return sorted(result, key=lambda x: x['days_left'])


def print_header(title):
    print("\n" + "="*55)
    print(f"  {title}")
    print("="*55)

def print_line():
    print("-"*55)


# ==================== CAMERA + OCR ====================
def capture_image_from_camera():
    """Take a photo using webcam"""
    if not OCR_AVAILABLE:
        print("\n  ❌ Camera/OCR not available!")
        return None
    
    print("\n  📸 Opening camera...")
    print("  Position the expiry date clearly in view")
    print("  Press SPACE to capture, ESC to cancel")
    
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("  ❌ Cannot open camera!")
        return None
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Show instructions on frame
        cv2.putText(frame, "SPACE: Capture | ESC: Cancel", 
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(frame, "Show expiry date clearly", 
                    (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        cv2.imshow('📸 Expiry Date Scanner - Building AI', frame)
        
        key = cv2.waitKey(1) & 0xFF
        if key == 32:  # SPACE
            # Save the image
            image_path = 'captured_product.jpg'
            cv2.imwrite(image_path, frame)
            cap.release()
            cv2.destroyAllWindows()
            return image_path
        elif key == 27:  # ESC
            cap.release()
            cv2.destroyAllWindows()
            return None
    
    cap.release()
    cv2.destroyAllWindows()
    return None


def read_expiry_from_image(image_path):
    """Read expiry date from image using OCR"""
    if not OCR_AVAILABLE:
        return None, "OCR not available"
    
    try:
        # Read image
        img = cv2.imread(image_path)
        
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Increase contrast
        gray = cv2.equalizeHist(gray)
        
        # Use Tesseract to read text
        text = pytesseract.image_to_string(gray)
        
        # Find date patterns
        date_patterns = [
            r'\d{4}[/\-\.]\d{2}[/\-\.]\d{2}',  # 2025/06/15
            r'\d{2}[/\-\.]\d{2}[/\-\.]\d{4}',  # 15/06/2025
        ]
        
        found_date = None
        for pattern in date_patterns:
            match = re.search(pattern, text)
            if match:
                date_str = match.group(0)
                # Try to parse
                for fmt in ['%Y/%m/%d', '%Y-%m-%d', '%Y.%m.%d', '%d/%m/%Y', '%d-%m-%Y', '%d.%m.%Y']:
                    try:
                        parsed = datetime.strptime(date_str, fmt)
                        found_date = parsed.strftime('%Y-%m-%d')
                        return found_date, text
                    except:
                        continue
        
        return None, text
    
    except Exception as e:
        return None, str(e)


# ==================== RECIPES ====================
RECIPES = {
    'milk': ['Rice Pudding', 'Pancakes', 'Custard', 'Mac and Cheese', 'Cream Soup'],
    'eggs': ['Omelette', 'French Toast', 'Scrambled Eggs', 'Boiled Eggs', 'Cake'],
    'bread': ['French Toast', 'Bread Pudding', 'Croutons', 'Grilled Cheese', 'Panzanella'],
    'chicken': ['Chicken Curry', 'Grilled Chicken', 'Chicken Soup', 'Stir Fry', 'Roast Chicken'],
    'tomato': ['Pasta Sauce', 'Tomato Salad', 'Shakshuka', 'Tomato Soup', 'Bruschetta'],
    'cheese': ['Grilled Cheese', 'Mac and Cheese', 'Cheese Omelette', 'Pizza', 'Fondue'],
    'banana': ['Banana Smoothie', 'Banana Bread', 'Banana Pancakes', 'Fruit Salad'],
    'yogurt': ['Smoothie', 'Tzatziki Dip', 'Marinade', 'Parfait', 'Raita'],
    'rice': ['Fried Rice', 'Rice Pudding', 'Risotto', 'Rice Soup', 'Biryani'],
    'pasta': ['Pasta Marinara', 'Pasta Salad', 'Baked Ziti', 'Carbonara', 'Pesto Pasta'],
    'fish': ['Grilled Fish', 'Fish Curry', 'Fish and Chips', 'Fish Soup'],
    'beef': ['Steak', 'Beef Stew', 'Burger', 'Meatballs', 'Stir Fry'],
    'carrot': ['Carrot Soup', 'Roasted Carrots', 'Carrot Cake', 'Salad'],
    'potato': ['Mashed Potatoes', 'Baked Potato', 'French Fries', 'Potato Soup'],
    'onion': ['French Onion Soup', 'Onion Rings', 'Caramelized Onions', 'Salad'],
    'butter': ['Cookies', 'Cake', 'Sauce', 'Garlic Bread', 'Pastry'],
    'cream': ['Pasta Sauce', 'Soup', 'Ice Cream', 'Whipped Cream', 'Curry'],
    'flour': ['Bread', 'Pizza Dough', 'Pancakes', 'Cake', 'Cookies'],
    'sugar': ['Cake', 'Cookies', 'Jam', 'Caramel', 'Sweet Tea'],
    'oil': ['Frying', 'Salad Dressing', 'Marinade', 'Roasting', 'Stir Fry'],
    'salt': ['Seasoning', 'Preserving', 'Brining', 'Pasta Water'],
    'pepper': ['Seasoning', 'Steak au Poivre', 'Marinade', 'Salad'],
    'garlic': ['Garlic Bread', 'Aioli', 'Marinade', 'Roasted Garlic', 'Pasta'],
    'lemon': ['Lemonade', 'Lemon Chicken', 'Salad Dressing', 'Lemon Cake'],
    'apple': ['Apple Pie', 'Apple Sauce', 'Baked Apple', 'Apple Smoothie'],
    'orange': ['Orange Juice', 'Orange Cake', 'Orange Chicken', 'Salad'],
    'lettuce': ['Salad', 'Wrap', 'Lettuce Cups', 'Burger Topping'],
    'cucumber': ['Salad', 'Tzatziki', 'Pickles', 'Sandwich'],
    'chocolate': ['Brownies', 'Hot Chocolate', 'Chocolate Cake', 'Mousse'],
    'coffee': ['Coffee', 'Tiramisu', 'Coffee Cake', 'Affogato'],
    'tea': ['Tea', 'Chai Latte', 'Iced Tea', 'Tea Cake'],
    'honey': ['Tea Sweetener', 'Marinade', 'Salad Dressing', 'Baking'],
    'jam': ['Toast', 'Pastry Filling', 'Yogurt Topping', 'Cake Filling'],
    'peanut butter': ['Sandwich', 'Cookies', 'Smoothie', 'Sauce'],
    'cereal': ['Breakfast Bowl', 'Cereal Bars', 'Topping', 'Snack Mix'],
    'juice': ['Drink', 'Smoothie', 'Popsicle', 'Marinade'],
    'soda': ['Drink', 'Float', 'Marinade', 'Cake'],
    'water': ['Drink', 'Cooking', 'Ice Cubes', 'Soup'],
}


def get_recipes(product_name):
    name = product_name.lower().strip()
    if name in RECIPES:
        return RECIPES[name]
    for key in RECIPES:
        if key in name or name in key:
            return RECIPES[key]
    return None


def search_recipe_online(product_name):
    """Open web browser to search for recipes"""
    query = product_name.replace(' ', '+') + '+recipe'
    url = f'https://www.google.com/search?q={query}'
    print(f"\n  🌐 Opening browser to search: {product_name} recipes")
    webbrowser.open(url)


def show_recipes(product_name):
    """Show recipes - local first, then offer online search"""
    recipes = get_recipes(product_name)
    
    print(f"\n  📖 Recipes for {product_name}:")
    print_line()
    
    if recipes:
        for i, recipe in enumerate(recipes, 1):
            print(f"  {i}. 🍳 {recipe}")
    else:
        print("  📭 No local recipes found.")
    
    print(f"\n  🌐 Search online for more recipes?")
    choice = input("  Search online? (y/n): ").strip().lower()
    if choice == 'y':
        search_recipe_online(product_name)


# ==================== ALARMS ====================
def check_alarms(product):
    """Check which alarms should trigger"""
    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    expiry = datetime.strptime(product['expiry'], '%Y-%m-%d')
    days_left = (expiry - today).days
    
    alarms = []
    
    if days_left == 7:
        alarms.append('🔔 7-DAY ALARM: Plan to use soon!')
    elif days_left == 4:
        alarms.append('🔔 4-DAY ALARM: Time to use!')
    elif days_left == 2:
        alarms.append('🔔 2-DAY ALARM: Use NOW!')
    elif days_left == 1:
        alarms.append('🚨 FINAL ALARM: Last day tomorrow!')
    elif days_left == 0:
        alarms.append('🚨 TODAY IS THE LAST DAY!')
    elif days_left < 0:
        alarms.append('❌ EXPIRED!')
    
    return alarms, days_left


# ==================== ADD PRODUCT ====================
def add_product_from_camera(db):
    """Add product by taking a photo"""
    print_header("📸 ADD PRODUCT FROM CAMERA")
    
    # Take photo
    image_path = capture_image_from_camera()
    
    if not image_path:
        print("  Cancelled.")
        return
    
    # Read date
    print("\n  🔍 Analyzing image...")
    found_date, raw_text = read_expiry_from_image(image_path)
    
    if found_date:
        print(f"  ✅ Date detected: {found_date}")
        print(f"  📝 Raw text found: {raw_text[:100]}...")
    else:
        print(f"  ⚠️  Could not automatically detect date.")
        print(f"  📝 Text found: {raw_text[:200]}")
        print(f"  You can enter the date manually.")
        found_date = ""
    
    # Let user confirm/correct
    print_line()
    print("  ✏️  Verify or correct the information:")
    print_line()
    
    name = input("  Product name: ").strip()
    expiry = input(f"  Expiry date [{found_date}]: ").strip()
    
    # Use detected date if user presses Enter
    if not expiry and found_date:
        expiry = found_date
    
    # Validate date
    try:
        datetime.strptime(expiry, '%Y-%m-%d')
    except:
        print("\n  ❌ Invalid date format! Use YYYY-MM-DD")
        return
    
    # Save
    product = db.add(name, expiry)
    alarms, days_left = check_alarms(product)
    
    print(f"\n  ✅ SAVED SUCCESSFULLY!")
    print(f"  📦 Product: {name}")
    print(f"  📅 Expires: {expiry}")
    print(f"  ⏳ Days left: {days_left}")
    print(f"  ⏰ Alarms set for:")
    print(f"     • 7 days before: {product['alarms']['7_days']}")
    print(f"     • 4 days before: {product['alarms']['4_days']}")
    print(f"     • 2 days before: {product['alarms']['2_days']}")
    
    if alarms:
        for alarm in alarms:
            print(f"  {alarm}")
    
    # Offer recipe
    print(f"\n  🍳 Would you like recipe suggestions for {name}?")
    choice = input("  Show recipes? (y/n): ").strip().lower()
    if choice == 'y':
        show_recipes(name)


def add_product_manual(db):
    """Add product manually"""
    print_header("✏️  ADD PRODUCT MANUALLY")
    
    name = input("  Product name: ").strip()
    expiry = input("  Expiry date (YYYY-MM-DD): ").strip()
    
    try:
        datetime.strptime(expiry, '%Y-%m-%d')
    except:
        print("\n  ❌ Invalid date! Use YYYY-MM-DD")
        return
    
    product = db.add(name, expiry)
    alarms, days_left = check_alarms(product)
    
    print(f"\n  ✅ SAVED!")
    print(f"  📦 {name} | 📅 {expiry} | ⏳ {days_left} days left")
    print(f"  ⏰ Alarms: 7 days, 4 days, 2 days before expiry")


# ==================== VIEW ====================
def view_all(db):
    print_header("📊 ALL PRODUCTS")
    products = db.get_all()
    
    if not products:
        print("  📭 No products yet.")
        return
    
    for i, p in enumerate(products, 1):
        alarms, days = check_alarms(p)
        
        if days < 0:
            emoji = "🔴"
        elif days <= 2:
            emoji = "🔴"
        elif days <= 4:
            emoji = "🟠"
        elif days <= 7:
            emoji = "🟡"
        else:
            emoji = "✅"
        
        print(f"  {i}. {emoji} {p['name']}")
        print(f"     📅 Expires: {p['expiry']} | ⏳ {days} days left")
        if alarms:
            for alarm in alarms:
                print(f"     {alarm}")
        print()


def check_expiring(db):
    print_header("⚠️  EXPIRING SOON (within 7 days)")
    expiring = db.get_expiring(7)
    
    if not expiring:
        print("  ✅ All good! No products expiring soon.")
        return
    
    for p in expiring:
        alarms, days = check_alarms(p)
        
        if days <= 2:
            emoji = "🔴 URGENT"
        elif days <= 4:
            emoji = "🟠 WARNING"
        elif days <= 7:
            emoji = "🟡 SOON"
        else:
            emoji = "✅"
        
        print(f"\n  {emoji}: {p['name']}")
        print(f"  📅 Expires: {p['expiry']} | ⏳ {days} days left")
        print(f"  ⏰ Alarm dates:")
        print(f"     • 7-day alarm: {p['alarms']['7_days']}")
        print(f"     • 4-day alarm: {p['alarms']['4_days']}")
        print(f"     • 2-day alarm: {p['alarms']['2_days']}")
        if alarms:
            for alarm in alarms:
                print(f"  {alarm}")
        print(f"  🍳 [Press 'r' for recipes, Enter to skip]")
    
    print_line()
    choice = input("  Show recipes for expiring products? (y/n): ").strip().lower()
    if choice == 'y':
        for p in expiring:
            show_recipes(p['name'])


def remove_product(db):
    print_header("🗑️  REMOVE PRODUCT")
    products = db.get_all()
    
    if not products:
        print("  No products.")
        return
    
    for i, p in enumerate(products, 1):
        alarms, days = check_alarms(p)
        print(f"  {i}. {p['name']} (expires: {p['expiry']}, {days} days)")
    
    try:
        idx = int(input("\n  Number to remove: ")) - 1
        if 0 <= idx < len(products):
            removed = db.products.pop(idx)
            db.save()
            print(f"  ✅ Removed: {removed['name']}")
        else:
            print("  ❌ Invalid!")
    except:
        print("  ❌ Invalid!")


# ==================== MAIN ====================
def main():
    db = ProductDatabase()
    
    print_header("📱 EXPIRY DATE TRACKER & RECIPE SUGGESTER")
    print("  Building AI Course Project")
    print("  📸 Camera OCR | ⏰ Smart Alarms | 🍳 Recipes")
    
    while True:
        print_header("MAIN MENU")
        print("  1. 📸 Scan product with camera (OCR)")
        print("  2. ✏️  Add product manually")
        print("  3. 📊 View all products")
        print("  4. ⚠️  Check expiring soon (7 days)")
        print("  5. 🍳 Get recipe suggestions")
        print("  6. 🔍 Search recipes online")
        print("  7. 🗑️  Remove a product")
        print("  8. 🚪 Exit")
        print_line()
        
        choice = input("  Choose (1-8): ").strip()
        
        if choice == '1':
            add_product_from_camera(db)
        elif choice == '2':
            add_product_manual(db)
        elif choice == '3':
            view_all(db)
        elif choice == '4':
            check_expiring(db)
        elif choice == '5':
            print_header("🍳 RECIPE SUGGESTIONS")
            name = input("  Product name: ").strip()
            show_recipes(name)
        elif choice == '6':
            print_header("🔍 SEARCH RECIPES ONLINE")
            name = input("  Product to search for: ").strip()
            search_recipe_online(name)
        elif choice == '7':
            remove_product(db)
        elif choice == '8':
            print_header("👋 GOODBYE!")
            print("  Reduce food waste, save money, eat well!")
            print("  Building AI Course Project")
            break
        else:
            print("\n  ❌ Invalid option!")
        
        input("\n  Press Enter to continue...")


if __name__ == "__main__":
    main()