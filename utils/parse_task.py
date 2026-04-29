import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


def parse_natural_language_task(user_input: str):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:8000",
        "X-Title": "Smart Task Manager"
    }

    prompt = f"""
Convert the following natural language task into clean JSON.

Return ONLY valid JSON.

Format:
{{
  "title": "...",
  "description": "...",
  "status": "pending"
}}

Input:
{user_input}
"""

    payload = {
        "model": "google/gemma-3-4b-it:free",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=30
        )

        print("STATUS:", response.status_code)
        print("RAW:", response.text)

        response.raise_for_status()

        result = response.json()
        content = result["choices"][0]["message"]["content"]

        # clean accidental markdown if model adds it
        content = content.replace("```json", "").replace("```", "").strip()

        parsed_task = json.loads(content)

        return parsed_task

    except Exception as e:
        print("AI Parsing Error:", str(e))

        return {
            "title": user_input[:50],
            "description": user_input,
            "status": "pending"
        }