# Expiry Date Tracker & Recipe Suggester

Final project for the Building AI course

## Summary

An intelligent system that uses AI and OCR technology to read expiration dates on food products through the phone camera. The system stores these dates, alerts the user before the product expires, and suggests recipes for products about to expire.

## Background

Food waste is a massive global problem. This system helps reduce waste by tracking expiration dates and sending smart alerts at 7, 4, and 2 days before expiry.

## How is it used?

1. Scan product with phone camera
2. AI reads expiry date
3. Correct date if needed
4. Enter product name
5. System saves and schedules alerts
6. Get alerts at 7, 4, and 2 days before expiry
7. Search recipes online for expiring products

## Data sources and AI methods

- OCR for reading dates from images
- Local storage for product database
- Web search for recipe suggestions
- PWA for mobile installation

## Challenges

- OCR accuracy depends on image quality
- Requires user to photograph products
- Internet needed for recipe search

## What next?

- Real OCR with Tesseract.js
- Native mobile app
- Barcode scanning
- Cloud sync

## Acknowledgments

- Building AI course by University of Helsinki and Reaktor
- Tesseract OCR project
- Open Food Facts
