import openai
import time

def get_mission():
    prompt = (
        "Create ONE short and simple Minecraft mission for two 8-year-olds, Cedar and Luke. "
        "The mission should be VERY easy to read - keep it to 8 words in a sentence or less - and involve a simple build of a structure or finding and mining 1 of a particular crafting block type. "
        "It should be able to be completed in any generated Minecraft world, so keep it vague. For example, 'find one wood block' or 'build a small boat'. "
        "After they complete the mission, give them a magical upgrade, skill, or weapon in ONE sentence. "
        "Make it very magical and exciting. ONLY give ONE mission and ONE upgrade. "
        "After giving the upgrade, prompt them to say 'We did it!' to get the next mission."
    )
    
    print("Thinking of a new magical mission...")
    time.sleep(2)  # Small pause for dramatic effect

    client = openai.OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=1,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    mission = response.choices[0].message.content.strip()
    # Clean up the response by removing any "Mission:" prefix
    mission = mission.replace("Mission:", "").strip()
    return mission

def main():
    print("🌟 Welcome to the Magical Minecraft Missions! 🌟")
    print("You and your cousin are about to embark on a magical adventure filled with enchanted powers and mystical quests!")

    # Start the first mission
    while True:
        print("\n✨ Your next mission is loading... ✨")
        mission = get_mission()
        
        # Separate mission from upgrade and clean up any empty lines
        mission_lines = [line.strip() for line in mission.split("\n") if line.strip()]
        current_mission = mission_lines[0] if mission_lines else "Error getting mission"
        upgrade = mission_lines[1] if len(mission_lines) > 1 else "You gained a magical power!"
        
        # Show the mission details
        print("\n🎮 Mission: ")
        print(current_mission)
        
        # Wait for the user to complete the mission
        done = input("\nType 'We did it!' when you complete this mission or 'Exit' to stop playing: ")
        
        if done.lower() == 'exit':
            print("Thanks for playing! See you next time, adventurers! 🚀")
            break
        elif done.lower() == 'we did it!':
            print("🎉 Awesome! You completed the mission! 🎉")
            print("✨ Reward: " + upgrade + " ✨")
            time.sleep(2)  # Short pause for excitement
            print("🪄 Preparing your next mission... 🪄")
            time.sleep(2)  # Dramatic pause before next mission

if __name__ == "__main__":
    main()
