"""AI Phishing Detector"""
import os
import sys
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

EMAIL = "email.txt"

EMAIL_CONTENT = ""

try:
    with open(EMAIL, "r", encoding="utf-8") as file:
        EMAIL_CONTENT = file.read()
    if not EMAIL_CONTENT.strip():
        print(f"Warning: The file '{EMAIL}' is empty or contains only whitespace.")
except FileNotFoundError:
    print(f"Error: The file '{EMAIL}' was not found. Please create it with email content.")
    sys.exit(1)
except Exception as e:
    print(f"An error occurred while reading the file: {e}")
    sys.exit(1)


prompt = f"""
Analyze the following email content for phishing indicators. Provide a percentage confidence score (e.g., "95%") on whether it is a phishing attempt. Also, briefly explain your reasoning, highlighting specific elements or patterns in the EMAIL that contribute to your assessment.

Email Content:
---
{EMAIL_CONTENT}
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
