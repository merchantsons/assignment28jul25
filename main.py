# main.py

import os
from dotenv import load_dotenv
import google.generativeai as genai

from context import context
from agents import triage_agent
from handoff import get_agent_by_label


load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=gemini_api_key)

def main():    
    print("---------------------------------- Multi-Agent Console Support System (By TechLoop) -----------------------------")
    print("👨‍🔧 You can say: 'I have a billing issue', 'App crashed', 'What is your address'.")
    print("🔁 It Can Automatically switch: 'switch to billing', 'switch to tech', 'switch to general' or 'switch to triage'.")
    print("❌ Type 'exit' or 'quit' to leave the chat.")
    print("-----------------------------------------------------------------------------------------------------------------")

    is_premium = input("Are you a premium user? (yes/no): ").strip().lower() == "yes"
    context["is_premium"] = is_premium

    current_agent = triage_agent

    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye! Thanks for using Console Support.")
            break

        if user_input.lower().startswith("switch to"):
            target = user_input.lower().replace("switch to", "").strip()
            new_agent = get_agent_by_label(target)
            if new_agent:
                current_agent = new_agent
                print(f"[System] 🔁 Switched to {current_agent.__name__.replace('_', ' ').title()}")
            else:
                print("[System] ⚠️ Unknown agent. Try 'switch to billing', 'switch to tech', or 'switch to triage'.")
            continue

   
        triage_result = triage_agent(user_input)

        if isinstance(triage_result, str) and triage_result.startswith("handoff_"):
            current_agent = get_agent_by_label(triage_result)
            print(f"[System] 🔁 Auto handoff triggered to {current_agent.__name__.replace('_', ' ').title()}")

        response = current_agent(user_input)


        if isinstance(response, str) and response.startswith("handoff_"):
            current_agent = get_agent_by_label(response)
            print(f"[System] 🔁 Handoff triggered by {current_agent.__name__.replace('_', ' ').title()} agent")
            continue

        print(f"{current_agent.__name__.replace('_', ' ').title()}: {response}")

if __name__ == "__main__":
    main()
