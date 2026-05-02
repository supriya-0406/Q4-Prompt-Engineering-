def generate_prompt(lead_name, company, notes):
    return f"""
You are a B2B sales assistant.

Lead: {lead_name} at {company}
Notes: {notes}

Write a professional 3-sentence follow-up email with:
- Reference to discussion
- Next step
- Clear CTA
"""
