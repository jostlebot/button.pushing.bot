import os
import openai
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

# Initialize the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Check if API key is loaded
if client.api_key is None:
    raise ValueError("API Key not found. Make sure OPENAI_API_KEY is set in your environment variables.")

# Make the API call
response = client.chat.completions.create(
    model="gpt-4o",  # Using gpt-4o model
    messages=[
        {
            "role": "system",
            "content": "You are a therapist ally specializing in assessing suicidal ideation using the wisdom and work of Jeffrey Sung, MD from UW"
        }
    ]
)
