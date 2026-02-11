# app/gemini_helper.py
import google.generativeai as genai
from dotenv import load_dotenv
import os
import traceback

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("❌ GEMINI_API_KEY not found in .env file!")

genai.configure(api_key=API_KEY)

def generate_answer(context_chunks, user_question):
    """
    Ye function Gemini API ko call karta hai aur 
    retrieved chunks ko context ke tor pe use karta hai.
    """
    try:
        model = genai.GenerativeModel("gemini-2.5-pro")

        context_text = "\n\n".join(context_chunks)

        prompt = f"""
You are a friendly travel assistant. Use the information below to answer
the user's question in a natural, conversational way.

If the answer is not in the context, simply say:
"I'm sorry, I don’t have that information right now."
        Context:
        {context_text}

        Question:
        {user_question}
        """

        response = model.generate_content(prompt)
        return response.text.strip()

    except Exception as e:
        print(f"❌ Gemini API Error: {e}")
        return f"Error: Unable to generate answer. Check server logs.{e}"
