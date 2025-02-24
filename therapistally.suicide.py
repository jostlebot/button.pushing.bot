import os
import openai

# Get API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Check if API key is loaded
if openai.api_key is None:
    raise ValueError("API Key not found. Make sure OPENAI_API_KEY is set in your environment variables.")

# Make the API call
response = openai.ChatCompletion.create(
    model="gpt-4o",  # Using gpt-4o model
    messages=[
        {
            "role": "system",
            "content": "You are a therapist ally specializing in assessing suicidal ideation using the wisdom and work of Jeffrey Sung, MD from UW
