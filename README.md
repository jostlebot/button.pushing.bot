# Button Pushing Bot - Therapeutic Conversation Tools

A collection of AI-powered conversation tools designed to help users explore and improve their interpersonal skills, distress tolerance, and communication patterns. These tools use OpenAI's latest API to create interactive experiences that challenge users in a controlled environment.

## Features

- **ButtonBot**: Helps users practice distress tolerance by simulating challenging conversations
- **ConvoCoach**: Assesses interpersonal skills and provides guided role-playing exercises
- **GuessWhoFromLuke**: A fun game for children to practice deduction and questioning
- **TherapistAlly**: Specialized tool for mental health professionals
- **Minecraft Missions**: Creative missions for children in Minecraft with rewards

## Setup

1. Clone this repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file based on the `.env.example` template and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

Each script can be run independently:

```bash
# Run the ButtonBot distress tolerance exercise
python buttonbot2.0.py

# Run the expanded guidance version with assessment
python buttonbotWITHexpandedGuidance.py

# Run the Minecraft mission generator
python simpleminecraft.mission.py

# Run the Guess Who game
python GuessWhoFromLuke.py
```

## About

This project explores the idea of therapeutic tools that place users in positions to explore and stretch their distress tolerance with an AI conversation partner. By creatively pressing the limits of the user's patterned behaviors (such as codependency), these tools aim to increase self-awareness and build resilience in a safe environment.
