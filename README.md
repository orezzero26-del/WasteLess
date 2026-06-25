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
I noticed that my family was throwing away a significant amount of food every week simply because we forgot what was in the fridge. I wanted to create a solution that uses technology to help us track our food better and minimize unnecessary waste.
# Expiry Date Tracker & Recipe Suggester 🍽️

Final project for the Building AI course

## Summary

An intelligent system that uses Optical Character Recognition (OCR) technology to read expiration dates on food products through the phone camera. The system stores these dates, alerts the user before the product expires, and suggests recipes that use the product that is about to expire.

## Problem Statement

### Why do we need this system?

* Many people buy products and forget their expiration dates
* Products are placed in the fridge without tracking when they should be consumed
* Users discover expired products when it is too late
* Food waste costs families hundreds of dollars annually
* There is no simple system that automatically reads dates and reminds users

### My Personal Motivation

In my household, we often find expired products in the fridge because we:
1. Didn't check the expiration date when purchasing
2. Forgot about the product in the corner of the fridge
3. Didn't know what to cook with it before it was too late

I wanted to build a simple system: just photograph the date, and it handles the rest!

## How It Works

### Step-by-Step Usage:

#### 1. Photograph the Expiration Date 📸

When purchasing a new product and before placing it in the fridge:
- The user opens the app
- Selects "Add New Product"
- Points the camera at the expiration date on the package
- The system automatically captures the image when the date is clear

#### 2. Automatic Date Reading 🔍

- The system uses **OCR** (Optical Character Recognition) technology
- Extracts the date from the image: Day / Month / Year
- Asks the user: "What is this product?" (select from list or type)
- User confirms: ✓ "Milk - Expires 2025/01/15"

#### 3. Storage and Scheduling 📊

The product is added to the database with:
- Product name
- Expiration date
- Date added
- Product image (optional)

The system sorts products by closest expiration date.

#### 4. Smart Alerts ⏰

Before the expiration date, the system sends alerts:

| Timing | Alert Type | Example |
|--------|------------|---------|
| 3 days before | 🟡 First Alert | "Milk will expire in 3 days" |
| 1 day before | 🟠 Second Alert | "Last chance! Milk expires tomorrow" |
| Last day | 🔴 Urgent Alert | "Today is the last day to use Milk" |

#### 5. Recipe Suggestions 👨‍🍳

With each alert, the system suggests a recipe using the product:
