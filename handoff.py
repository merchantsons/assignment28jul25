# handoff.py

from agents import triage_agent, billing_agent, tech_agent, general_agent

def get_agent_by_label(label: str):
    label = label.lower().strip()
    
    if "billing" in label:
        return billing_agent
    elif "tech" in label or "technical" in label:
        return tech_agent
    elif "general" in label or "support" in label:
        return general_agent
    elif "triage" in label:
        return triage_agent
    else:
        return None
