import pytesseract
from PIL import Image
import openai
import os  
import json
import pandas as pd

# Set up Tesseract executable path (update this based on your system)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Windows

# OpenAI API Key
openai.api_key = " "   

def extract_text_from_image(image_path):
    """
    Extracts text from a single image using Tesseract.
    """
    try:
        print(f"Extracting text from: {image_path}")
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return ""

def process_images(image_paths):
    """
    Processes multiple images and combines extracted text.
    """
    combined_text = ""
    for image_path in image_paths:
        print(f"Processing image: {image_path}")
        extracted_text = extract_text_from_image(image_path)
        print(f"Extracted text from {image_path}:\n{extracted_text}\n")
        if extracted_text:
            combined_text += extracted_text + "\n\n"  # Separate text from different images
    return combined_text

def extract_info_with_openai(text):
    """
    Sends extracted text to OpenAI API and retrieves structured information.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a resume and LinkedIn profile parser. Extract key information in JSON format."},
                {"role": "user", "content": f"Extract structured information from the following text:\n{text}"}
            ],
            max_tokens=1500
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"Error with OpenAI API: {e}")
        return ""

def generate_summary(info):
    """
    Generates a short summary of the person based on their profile information.
    """
    try:
        print("Generating a profile summary...")
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an assistant that creates professional summaries of people based on LinkedIn profiles."},
                {
                    "role": "user",
                    "content": f"""Using the following structured information, write a concise professional summary:

{info}"""
                }
            ],
            max_tokens=200
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"Error with OpenAI API while generating summary: {e}")
        return ""

def generate_connection_note(info):
    """
    Generates a targeted connection note using OpenAI API based on the extracted information.
    """
    try:
        print("Generating a connection note...")
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a professional assistant. Write polite and engaging LinkedIn connection notes."},
                {
                    "role": "user",
                    "content": f"""Based on the following information, write a connection note:

{info}"""
                }
            ],
            max_tokens=300
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"Error with OpenAI API while generating connection note: {e}")
        return ""

def save_to_csv(data, output_file="linkedin_output.csv"):
    """
    Saves extracted data to a CSV file.
    """
    df = pd.DataFrame(data)
    if not os.path.exists(output_file):
        # Create file and add headers
        df.to_csv(output_file, index=False, mode="w")
    else:
        # Append to existing file
        df.to_csv(output_file, index=False, mode="a", header=False)
    print(f"Data saved to {output_file}")

def main():
    # Path to the directory containing LinkedIn screenshot images
    image_directory = r"C:"  # Use the correct folder path
    
    print(f"Looking for images in: {image_directory}")
    
    # Get all image files from the directory
    try:
        image_paths = [os.path.join(image_directory, img) for img in os.listdir(image_directory) if img.endswith(('.png', '.jpg', '.jpeg'))]
        print(f"Found {len(image_paths)} image(s): {image_paths}")
    except Exception as e:
        print(f"Error reading directory: {e}")
        return
    
    if not image_paths:
        print("No images found in the directory. Please add LinkedIn screenshots.")
        return
    
    print("Extracting text from images...")
    combined_text = process_images(image_paths)
    
    if not combined_text.strip():
        print("No text extracted. Ensure the images are clear and Tesseract is set up correctly.")
        return
    
    print("Text extracted successfully. Sending to OpenAI...")
    structured_info = extract_info_with_openai(combined_text)
    
    if structured_info:
        print("\nExtracted Information:")
        print(structured_info)
        
        # Generate a professional summary
        summary = generate_summary(structured_info)
        if summary:
            print("\nProfessional Summary:")
            print(summary)
        else:
            print("No summary could be generated.")
        
        # Generate a targeted connection note for McLaren Strategic Ventures
        connection_note = generate_connection_note(structured_info)
        if connection_note:
            print("\nGenerated Connection Note:")
            print(connection_note)
        else:
            print("No connection note could be generated.")
        
        # Save data to CSV
        output_data = [
            {
                "Structured Info": structured_info,
                "Summary": summary,
                "Connection Note": connection_note
            }
        ]
        save_to_csv(output_data)
    else:
        print("No structured information could be extracted.")

if __name__ == "__main__":
    main()
