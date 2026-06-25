# Expiry Date Tracker & Recipe Suggester

Final project for the Building AI course project

## Summary

An intelligent mobile app that uses AI and OCR to read expiration dates on food products from photos. The app stores dates, sends smart alerts 7, 4, and 2 days before expiry, and suggests online recipes for products about to expire.

## Background

Food waste is a massive global problem:
* 1.3 billion tons of food wasted annually worldwide
* Households throw away 30% of purchased food
* Average family loses $1500 per year on wasted food

My personal motivation: I often find expired products in my fridge because I forgot they were there. I wanted a simple app that reads expiry dates from photos and reminds me before food goes bad.

## How is it used?

The solution is used at home, in the kitchen, when putting away groceries:

1. User opens the app on their phone
2. Takes a photo of the expiry date on the product
3. AI reads the date automatically using OCR
4. User can correct the date if the AI made an error
5. User enters the product name
6. App saves the product and schedules alarms
7. User receives alerts at 7, 4, and 2 days before expiry
8. With each alert, user can search recipes online

Users: Families, students, elderly people, restaurants, anyone who buys groceries.
def check_alert(name, expiry_str):
expiry = datetime.strptime(expiry_str, '%Y-%m-%d')
today = datetime.now()
days = (expiry - today).days

if days <= 0:
return 'EXPIRED!'
elif days <= 2:
return f'Use TODAY!'
elif days <= 4:
return f'Use soon!'
elif days <= 7:
return f'Plan to use!'
return f'Good for {days} days'

## Data sources and AI methods

Data sources:
* User input: product names and expiry dates
* Device camera: photos of product labels
* Web search: recipe suggestions

AI methods:

| Method | Application |
|--------|-------------|
| OCR | Reading expiry dates from images |
| Date parsing | Understanding various date formats |
| Local database | Storing products on device |
| PWA technology | Installing as mobile app |

## Challenges

What this project does not solve:
* Cannot read dates on damaged labels
* Does not handle products without printed dates
* Requires manual photographing of each product
* OCR accuracy varies with camera quality

Ethical considerations:
* User data stored locally for privacy
* No personal data collected or shared
* Accessible design for all ages

## What next?

To grow this project:
* Integrate real OCR with Tesseract.js
* Build native mobile app with Flutter
* Add barcode scanning
* Cloud sync for family sharing
* Voice input support

Skills needed: Flutter, TensorFlow, cloud computing, UX design.

## Acknowledgments

* Building AI course by University of Helsinki and Reaktor
* Tesseract OCR open source project
* Open Food Facts database
* Inspiration from my own kitchen experience