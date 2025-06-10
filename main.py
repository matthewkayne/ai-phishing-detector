import os, sys
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

email = "email.txt"

email_content = ""

try:
    with open(email, "r", encoding="utf-8") as file:
        email_content = file.read()
    if not email_content.strip():
        print(f"Warning: The file '{email}' is empty or contains only whitespace.")
except FileNotFoundError:
    print(f"Error: The file '{email}' was not found. Please create it with email content.")
    sys.exit()
except Exception as e:
    print(f"An error occurred while reading the file: {e}")
    sys.exit()


prompt = f"""
Analyze the following email content for phishing indicators. Provide a percentage confidence score (e.g., "95%") on whether it is a phishing attempt. Also, briefly explain your reasoning, highlighting specific elements or patterns in the email that contribute to your assessment.

Email Content:
---
{email_content}
---
"""

try:
    model = genai.GenerativeModel('gemini-1.5-flash')
    print("Sending request to Gemini API...")
    response = model.generate_content(prompt)
 
    print("\n--- Phishing Assessment ---")
    print(response.text)
    print("---------------------------\n")

except Exception as e:
    print(f"An error occurred while calling the Gemini API: {e}")
    print("Please ensure your API key is correct and you have network connectivity.")