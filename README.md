# LinkedIn-Profile-Parser

Overview

This Python script extracts text from LinkedIn profile screenshots using Optical Character Recognition (OCR) and processes it using OpenAI's GPT-4 model. It then generates structured information, a professional summary, and a LinkedIn connection note tailored to setting up a meeting with McLaren Strategic Ventures.

Features

Extracts text from multiple LinkedIn profile screenshots.

Uses OpenAI's GPT-4 to analyze and structure profile data.

Generates a professional summary.

Creates a personalized LinkedIn connection note.

Saves extracted data to a CSV file.

Requirements

Python 3.x

Tesseract-OCR installed and configured

OpenAI API key

Required Python libraries:

pytesseract

PIL (Pillow)

openai

os

json

pandas

Installation

Install Python 3.x if not already installed.

Install Tesseract-OCR:

Windows: Download and install from Tesseract GitHub.

macOS: Install via Homebrew:

brew install tesseract

Linux: Install using package manager:

sudo apt install tesseract-ocr

Install required Python packages:

pip install pytesseract pillow openai pandas

Set up your OpenAI API key:

Replace openai.api_key = " " in the script with your API key.

Usage

Place LinkedIn profile screenshots in the specified directory (update image_directory in the script).

Run the script:

python linkedin_parser.py

The extracted information, summary, and connection note will be displayed and saved to linkedin_output.csv.

Output

Structured Information: Extracted key details from the LinkedIn profile.

Professional Summary: A brief summary of the person’s background.

Connection Note: A personalized message for reaching out on LinkedIn.

Notes

Ensure screenshots are clear for accurate OCR extraction.

If errors occur, verify Tesseract-OCR is installed and properly configured.

Modify generate_connection_note to customize the messaging for different companies.

License

This project is for personal and professional use. Modify as needed!
