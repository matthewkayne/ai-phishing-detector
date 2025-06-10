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


PROMPT = f"""
Analyze the following email content for phishing indicators. Provide a percentage confidence score (e.g., "95%") on whether it is a phishing attempt. Also, briefly explain your reasoning, highlighting specific elements or patterns in the EMAIL that contribute to your assessment.

Email Content:
---
{EMAIL_CONTENT}
---
"""

model = genai.GenerativeModel('gemini-1.5-flash')
print("Sending request to Gemini API...")
response = model.generate_content(PROMPT)

print("\n--- Phishing Assessment ---")
print(response.text)
print("---------------------------\n")

def get_confirmation(prompt_message):

    while True:
        user_input = input(prompt_message + " (y/n): ").strip().lower()

        if user_input in ["y", "yes", "Y", "Yes"]:
            return True
        elif user_input in ["n", "no", "N", "No"]:
            return False
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")



if get_confirmation("Would you like to download this report?" ) is True:
    print()
    report_file="report.txt"
    try:
        with open(report_file, 'w', encoding='utf-8') as file:
            file.write(response.text)
            print("---------------------------\n")
            print(f"Successfully created/overwrote '{report_file}' with new content.\n")
    except IOError as e:
        print(f"Error writing to file '{report_file}': {e}")
       
else:
    print()

print("---------------------------\n")
print("Thank you for using AI Phishing Detector")
