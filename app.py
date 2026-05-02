# q4_prompt.py — Prompt Engineering Example

SYSTEM_PROMPT = """
You are a B2B sales assistant.

Task:
Write a personalized 3-sentence follow-up email.

Rules:
1. Professional and warm tone
2. Must include:
   - Reference to discussion
   - Next step with timeline
   - Clear call-to-action
3. Output only email text (no JSON, no subject)
"""

def build_prompt(lead_name: str, company: str, meeting_notes: str) -> str:
    """Creates a structured prompt for the AI model"""

    user_prompt = f"""
Lead: {lead_name} at {company}
Meeting Notes: {meeting_notes}

Generate the follow-up email.
"""

    return SYSTEM_PROMPT + "\n" + user_prompt


# TEST RUN
if __name__ == "__main__":
    notes = "Discussed analytics module and demo scheduling"
    
    prompt = build_prompt(
        lead_name="Raj Patel",
        company="Acme Corp",
        meeting_notes=notes
    )

    print("🧠 Generated Prompt:\n")
    print(prompt)
