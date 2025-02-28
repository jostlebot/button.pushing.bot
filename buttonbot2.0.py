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

response = client.chat.completions.create(
  model="gpt-4o",  # Updated to latest model
  messages=[
    {
      "role": "system",
      "content": "you are a chat bot that is having a conversation with me and i need you to stretch the limits of my distress tolerance. ask me how my day was but then do a bad job of listening. interrupt me, get sidetracked, generally be rude and impatient. my goal will be to feel how the inflammation grows in me and to breathe deeply. explain up front that my goal is to expand my distress tolerance for future conversations in my real life."
    },
    {
      "role": "assistant",
      "content": "Sure! This exercise is designed to help you expand your distress tolerance for future conversations. Remember, the goal is to notice your reactions, practice deep breathing, and build resilience. Let's get started.\n\nHey there! How was your day?"
    }
  ],
  temperature=1,
  max_tokens=2048,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response.choices[0].message.content)
