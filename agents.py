# agents.py

from tools import billing_tool, tech_tool, general_tool
from context import context
import google.generativeai as genai

model = genai.GenerativeModel("gemini-1.5-flash")

def triage_agent(user_input):
    lowered = user_input.lower()
    if any(word in lowered for word in ["bill", "invoice", "payment", "charge"]):
        context["issue_type"] = "billing"
        return "handoff_billing"
    elif any(word in lowered for word in ["error", "crash", "slow", "bug"]):
        context["issue_type"] = "technical"
        return "handoff_tech"
    elif any(word in lowered for word in ["help", "support", "contact", "address"]):
        context["issue_type"] = "general"
        return "handoff_general"
    else:
        response = model.generate_content(
            f"Triage this user request in a customer support setting: '{user_input}'"
        )
        return f"👨‍🔧 General Support Agent: {response.text.strip()}"

def billing_agent(user_input):
    return billing_tool(context, user_input)

def tech_agent(user_input):
    return tech_tool(context, user_input)

def general_agent(user_input):
    return general_tool(context, user_input)
