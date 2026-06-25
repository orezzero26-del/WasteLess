
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


#WasteLess
AI-Powered Food Waste Reduction System 🍽️

The final project for the Building AI course.

Project Summary
An intelligent system that leverages Artificial Intelligence and Machine Learning technologies to reduce food waste in households and restaurants. The system tracks stored food items, predicts expiration dates, and suggests recipes to utilize ingredients before they spoil.

The Problem
1.3 billion tons of food are wasted globally every year.

Households dispose of approximately 30% of their food.

Food waste costs the average family around $1,500 annually.

Decomposing food in landfills releases methane gas, which is harmful to the environment.

Personal Motivation
I noticed that my family was throwing away a significant amount of food every week simply because we forgot what was in the fridge. I wanted to create a solution that uses technology to help us track our food better and minimize unnecessary waste.How does the system work?Steps:Fridge Scanning 📸The user takes a photo of the fridge contents.The system uses Computer Vision to identify the food items.Registering Purchases 🛒Users can input the purchase date and expiration date.The system tracks each food item.Spoilage Prediction ⏰Artificial Intelligence calculates the remaining shelf life for each item.It sends notifications two days before the expiration date.Recipe Suggestions 👨‍🍳It suggests recipes using ingredients close to expiration.It considers the user's dietary preferences.Target Users:UserBenefit🏠 FamiliesReduce monthly grocery expenses🍳 RestaurantsImprove inventory management🏫 School CanteensBetter meal planning🏪 Grocery StoresReduce product wasteData Sources and AI TechnologiesData Sources:SourceDescriptionLinkOpen Food FactsOpen database for food productsworld.openfoodfacts.orgUSDA FoodDataNutritional information and food characteristicsfdc.nal.usda.govUser DataCollected with user consent to improve predictions-AI Technologies Used:TechnologyUsageComputer Vision (CNN)Recognizing food from imagesNatural Language Processing (NLP)Parsing shopping lists and receiptsPredictive Machine LearningPredicting food spoilage datesRecommendation SystemsSuggesting appropriate cooking recipesTime Series AnalysisTracking consumption patternsProposed Model Architecture:Pre-trained CNN (MobileNetV2) for food recognition.LSTM network for predicting spoilage schedules.Collaborative filtering system for recipe recommendations.ChallengesWhat this project does not solve:Does not address major food supply chain issues.Requires user interaction for data entry.Might not recognize all local foods initially.Cannot handle unexpected power outages.Ethical Considerations:ConsiderationAction Taken🔒 User PrivacyData is stored securely and encrypted⚖️ Data BiasTraining the model on diverse cultural foods♿ AccessibilityDesigning an interface suitable for all users🔐 Data SecurityNo sharing of data with third partiesWhat's Next?To expand the project, I need:Development Skills:Mobile App Development (Flutter or React Native)Optimizing Computer Vision modelsLearning cloud computing for deploymentUser Experience (UX) designFuture Expansions:Partnering with grocery stores for direct integration.Linking with food banks to donate excess food.Integration with smart fridges.Adding a food-sharing feature for neighbors.Potential Collaborators:Environmental organizationsMajor retail chainsSmart appliance manufacturersLocal food banksAcknowledgmentsInspiration from the FAO food waste database.Computer Vision concepts from Building AI course exercises.Open Food Facts for their open database.Special thanks to the Building AI instructors for the fundamental knowledge.Motivation from my family's journey in reducing food waste.

