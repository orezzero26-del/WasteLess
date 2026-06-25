\# Expiry Date Tracker \& Recipe Suggester



Final project for the Building AI course



\## Summary



An intelligent system that uses AI and OCR technology to read expiration dates on food products through the phone camera. The system stores these dates, alerts the user before the product expires (7 days, 4 days, and 2 days before), and suggests recipes that use the product that is about to expire. Users can scan products with their camera or add them manually, with the ability to correct any AI-detected dates.



\## Background



Food waste is a massive global problem. Many people buy products and forget their expiration dates. This system solves this by:

\- Automatically reading expiry dates from product photos

\- Sending smart alerts at 7, 4, and 2 days before expiry

\- Suggesting recipes for products about to expire

\- Allowing manual correction if AI makes an error



\## How is it used?



1\. User scans a product's expiry date with their phone camera

2\. AI reads the date automatically

3\. User can correct the date if needed

4\. User enters the product name

5\. System saves the product and schedules alerts

6\. At 7, 4, and 2 days before expiry, user gets alerts

7\. With each alert, user can search for recipes online



\## Data sources and AI methods



\- OCR (Optical Character Recognition) for reading dates

\- Local storage for product database

\- Web search integration for recipe suggestions

\- PWA technology for mobile app installation



\## Challenges



\- OCR accuracy depends on image quality

\- Requires user to photograph each product

\- Does not handle products without printed expiry dates

\- Internet connection needed for recipe search



\## What next?



\- Real OCR integration with Tesseract.js or Google ML Kit

\- Native mobile app with Flutter

\- Barcode scanning for automatic product identification

\- Cloud sync across devices

\- Voice input for product names



\## Acknowledgments



\- Building AI course by University of Helsinki and Reaktor

\- Tesseract OCR project

\- Open Food Facts

