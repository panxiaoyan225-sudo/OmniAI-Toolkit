import os
from google import genai
from dotenv import load_dotenv, find_dotenv

# 1. LOAD CONFIGURATION
# find_dotenv() must have () to work correctly
# MySQL credentials
load_dotenv(find_dotenv())
# Wrap your key in quotes so Python sees it as text

api_key = os.getenv("GEMINI_API_KEY")

# Initialize the client
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.0-flash", 
    contents="when is canadan election"
)

print(response.text)