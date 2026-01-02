from fastapi import FastAPI
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

app = FastAPI(title="Essay Evaluation API")

class EssayInput(BaseModel):
    content: str

@app.get("/")
def home():
    return {"status": "ok", "message": "Essay Evaluation API Ready"}

@app.post("/evaluate")
async def evaluate_essay(data: EssayInput):
    parts = data.content.split("$")
    question = parts[1].strip()
    answer = parts[2].strip()
    
    model = genai.GenerativeModel("gemini-2.5-flash")
    
    prompt = f"""Evaluate if the answer relates to the question.

Question: {question}

Answer: {answer}

If the answer does NOT relate to the question, respond with: 0
If the answer relates to the question, respond with a mark between 1 to 100 based on accuracy and completeness.

Respond ONLY with a number (0-100), nothing else."""
    
    response = model.generate_content(prompt)
    mark = int(response.text.strip())
    
    return {"mark": mark}