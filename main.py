from fastapi import FastAPI
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
os.environ["GOOGLE_API_KEY"] = GEMINI_API_KEY

app = FastAPI(title="Essay Evaluation API")

class EssayInput(BaseModel):
    content: str

@app.get("/")
def home():
    return {"status": "ok", "message": "Essay Evaluation API Ready"}

@app.post("/evaluate")
async def evaluate_essay(data: EssayInput):
    # Parse input: $Question$Answer
    parts = data.content.split("$")
    question = parts[1].strip()
    answer = parts[2].strip()
    
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.1,
        api_key=GEMINI_API_KEY
    )
    
    prompt = f"""Evaluate if the answer relates to the question.

Question: {question}

Answer: {answer}

If the answer does NOT relate to the question, respond with: 0
If the answer relates to the question, respond with a mark between 1 to 100 based on accuracy and completeness.

Respond ONLY with a number (0-100), nothing else."""
    
    response = llm.invoke(prompt)
    mark = int(response.content.strip())
    
    return {"mark": mark}