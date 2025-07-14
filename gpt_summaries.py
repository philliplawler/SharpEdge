import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_summary(matchup: str, odds: dict) -> str:
    prompt = (
        f"Analyze the betting matchup: {matchup}.\n"
        f"Current odds are: {odds}.\n"
        f"Give a concise betting summary including any value or angles."
    )
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"GPT Error: {e}"
