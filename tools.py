def billing_tool(context, query):
    if context["issue_type"] == "billing":
        return (
            "💳 Premium Billing Support: Your account is in good standing. No dues."
            if context["is_premium"]
            else "💳 Standard Billing: You currently owe $20."
        )
    return "Billing tool is not enabled for this issue."

def tech_tool(context, query):
    if context["issue_type"] == "technical":
        return (
            "🛠️ Troubleshooting steps:\n"
            "- Restart the app\n"
            "- Check your internet connection\n"
            "- If issues persist, reinstall the app."
        )
    return "Tech support tool is not enabled for this issue."

def general_tool(context, query):
    if context["issue_type"] == "general":
        return (
            "Feel Free To Visit Our Address Is : \n"
            "- 123 Support St, Help City, HC 12345\n"
            "- Phone: (123) 456-7890\n"
            "- Email: support@example.com"
        )
    return "General support tool is not enabled for this issue."