"""
chatbot.py  —  Step 2

This is the exact same logic you already tested cell-by-cell in
01_explore_chatbot.ipynb, just saved as a plain .py file so the app
(Step 3) can import it.

How to run this file on its own, in VS Code:
  1. Open this file in VS Code.
  2. Click the "Run Python File" triangle button top-right (or press F5).
  3. Look at the terminal at the bottom — you should see a real reply
     printed for the test question at the bottom of this file.

If you see "WARNING: GROQ_API_KEY is not set" instead of a reply,
check that your .env file (same folder) has your real key in it.
"""

import os
from groq import Groq
from dotenv import load_dotenv

from pathlib import Path

env_path = Path(__file__).parent / ".env"
print("Looking for .env at:", env_path)
print(".env exists:", env_path.exists())

load_dotenv(env_path)

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
print("Key found:", bool(GROQ_API_KEY))

if not GROQ_API_KEY:
    print("WARNING: GROQ_API_KEY is not set. Add it to a .env file in this folder.")

client = Groq(api_key=GROQ_API_KEY) if GROQ_API_KEY else None

MODEL = "llama-3.3-70b-versatile"

SYSTEM_PROMPT = "You are a helpful, concise assistant. Keep answers short unless asked for detail."


def get_response(user_message: str) -> str:
    if not user_message or not user_message.strip():
        return "Please enter a message."

    if client is None:
        return "Server misconfiguration: GROQ_API_KEY is not set."

    try:
        completion = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message},
            ],
            temperature=0.7,
            max_tokens=512,
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error calling LLM: {e}"


if __name__ == "__main__":
    # This block only runs when you execute chatbot.py directly
    # (VS Code's "Run Python File" button, or `python chatbot.py`).
    test_question = "What is 2 + 2?"
    print(f"Test question: {test_question}")
    print("Reply:", get_response(test_question))
