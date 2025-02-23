import openai
import os

# Set your OpenAI API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
    model="gpt-4-turbo",  # Use the latest GPT-4 model
    messages=[
        {
            "role": "system",
            "content": (
                "You are an assistant called MENTAL HEALTH TRAINER for a user to have a conversation with. "
                "Be the trainer and let the user respond and relate to you. Trainer and user will interact in a way "
                "that replicates Monty Python's sketch 'Argument Clinic.' The Assistant will welcome the user and invite "
                "them to set the frame for the conversation. Respond only if the user says something to you and do so in the style of: "
                "\n\nMan: Is this the right room for an argument? "
                "\nOther Man: (pause) I've told you once. "
                "\nMan: No you haven't."
            )
        },
        {
            "role": "assistant",
            "content": "Welcome! Is this the right room for an argument?"
        }
    ],
    temperature=1,
    max_tokens=2048,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

# Print the assistant's response
print(response['choices'][0]['message']['content'])
