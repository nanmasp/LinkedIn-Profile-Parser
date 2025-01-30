# LinkedIn Profile Parser

## Overview
This Python script extracts text from LinkedIn profile screenshots using Optical Character Recognition (OCR) and processes it using OpenAI's GPT-4 model. It then generates structured information, a professional summary, and a LinkedIn connection note tailored to the person.

## Features
- Extracts text from multiple LinkedIn profile screenshots.
- Uses OpenAI's GPT-4 to analyze and structure profile data.
- Generates a professional summary.
- Creates a personalized LinkedIn connection note.
- Saves extracted data to a CSV file.

## Requirements
- **Python 3.x**
- **Tesseract-OCR** installed and configured
- **OpenAI API key**
- Required Python libraries:
  
  ```bash
  pip install pytesseract pillow openai pandas
  ```

## Installation
### Install Tesseract-OCR
- **Windows**: Download and install from [Tesseract GitHub](https://github.com/UB-Mannheim/tesseract/wiki).
- **macOS**: Install via Homebrew:
  
  ```bash
  brew install tesseract
  ```
- **Linux**: Install using package manager:
  
  ```bash
  sudo apt install tesseract-ocr
  ```

### Clone the Repository

```bash
git clone https://github.com/yourusername/linkedin-profile-parser.git
cd linkedin-profile-parser
```

### Set Up OpenAI API Key
Replace `openai.api_key = " "` in the script with your OpenAI API key.

## Usage
1. Place LinkedIn profile screenshots in the specified directory (update `image_directory` in the script).
2. Run the script:
   
   ```bash
   python linkedin_parser.py
   ```
3. The extracted information, summary, and connection note will be displayed and saved to `linkedin_output.csv`.

## Output
- **Structured Information:** Extracted key details from the LinkedIn profile.
- **Professional Summary:** A brief summary of the person’s background.
- **Connection Note:** A personalized message for reaching out on LinkedIn.

## Issues Encountered & Fixes
### 1. Setting Up Tesseract Path
**Issue:** Initially, the script could not detect Tesseract-OCR.
**Fix:** Manually set the Tesseract path in the script:
  ```python
  pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
  ```

### 2. Text Extraction Accuracy
**Issue:** Extracted text contained excessive noise or missing characters.
**Fix:** Preprocessed images by converting them to grayscale and increasing contrast to improve OCR accuracy.

### 3. Handling OpenAI API Rate Limits
**Issue:** Received `RateLimitError` while making API requests.
**Fix:** Implemented exponential backoff retry logic to handle rate limits more gracefully.

### 4. Structuring Extracted Information
**Issue:** The raw extracted text was unstructured and difficult to parse.
**Fix:** Used OpenAI’s API to generate structured JSON output and formatted it before saving.

### 5. Saving Data to CSV
**Issue:** The extracted information was incorrectly formatted in the CSV file.
**Fix:** Ensured the data was converted into a Pandas DataFrame before writing to the CSV.

## Notes
- Ensure screenshots are clear for accurate OCR extraction.
- If errors occur, verify Tesseract-OCR is installed and properly configured.
- Modify `generate_connection_note` to customize the messaging for whatever your use case is.

