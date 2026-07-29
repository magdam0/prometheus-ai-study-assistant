import os

from dotenv import load_dotenv
from google import genai

MODEL = "gemini-3.6-flash"

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def ask_llm(prompt):
    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
    )

    return response.text
