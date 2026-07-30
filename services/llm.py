import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

MODEL = "gemini-3.6-flash"

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def ask_llm(prompt, response_schema=None):
    config = None
    if response_schema is not None:
        config = types.GenerateContentConfig(
            response_mime_type="application/json",
            response_json_schema=response_schema,
        )

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
        config=config,
    )

    return response.text
