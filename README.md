# 🤖 Tophawks Q4: Customer Support Triage Prompt

Engineered system prompt for automated ticket routing, sentiment classification, and draft response generation. Forces **strict JSON output** for zero-parsing failures in downstream CRM/ticketing systems.

## ✨ Key Design Choices
- **Strict JSON Enforcement**: Explicit schema + "no extra text" rule guarantees 100% valid output
- **Edge-Case Fallback**: Ambiguous inputs → `Sentiment=3`, `Root_Issue="needs clarification"`
- **Anti-Hallucination**: Explicitly blocks inventing account numbers, technical details, or ungrounded promises
- **SLA-Aligned**: Mandates concrete next steps + clear timeframes in every draft response

## 🚀 How to Test
1. Open [OpenAI Playground](https://platform.openai.com/playground)
2. Paste the system prompt from `prompt_system.txt` into the **System** field
3. Use sample complaint as **User** input
4. Set `temperature=0`, `response_format={"type": "json_object"}`
5. Click **Run** → Verify valid JSON output

## ✅ Expected Output
```json
{
  "Sentiment": 1,
  "Root_Issue": "platform reliability incident",
  "Draft_Response": "I sincerely apologize for the disruption during your critical demo. I'm escalating this to our engineering lead and will contact you within 1 hour with a resolution plan and compensation options."
}
