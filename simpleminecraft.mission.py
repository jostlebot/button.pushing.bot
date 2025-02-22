import openai

def get_mission():
    prompt = (
        "Create a short and simple Minecraft mission for two 8-year-olds, Cedar and Luke. "
        "The mission should be VERY easy to read - keep it to 8 words in a sentence or less - and involve a simple build of a structure or finding and mining 1 of a particular crafting block type. "
        "It should be able to be completed in any generated Minecraft world, so keep it vague. For example, 'find one wood block' or 'build a small boat'. "
        "Once they complete a mission, tell them they have received a unique upgrade, skill, or weapon. "
        "Keep the language simple and make it very magical and exciting. "
        "At the end of the mission, prompt them to say 'We did it!' once completed to receive the next mission."
    )
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=1,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    mission = response['choices'][0]['message']['content']
    return mission

def main():
    print("Welcome to the Magical Minecraft Missions!")
    while True:
        print("\nYour next mission:")
        print(get_mission())
        
        done = input("\nType 'We did it!' when you complete this mission or 'Exit' to stop playing: ")
        
        if done.lower() == 'exit':
        
