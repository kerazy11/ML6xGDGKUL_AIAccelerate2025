import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def clean_with_gemini(sentence: str) -> str:
    prompt = f"Please rewrite this sentence using correct grammar and spelling: \"{sentence}\""
    response = model.generate_content(prompt)
    return response.text.strip()
