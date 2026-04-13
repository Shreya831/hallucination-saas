from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class Input(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "TruthGuard AI running 🚀"}


# -------- Answer (better than dummy) --------
def generate_answer(question):
    try:
        url = "https://api.duckduckgo.com/"
        params = {"q": question, "format": "json"}
        res = requests.get(url, params=params).json()

        if res.get("AbstractText"):
            return res["AbstractText"]

        return "No clear answer found."
    except:
        return "Error generating answer."


# -------- Evidence --------
def get_evidence(query):
    return generate_answer(query)


# -------- Better similarity --------
def compute_score(answer, evidence):
    a = set(answer.lower().split())
    b = set(evidence.lower().split())

    if not a:
        return 0.0

    overlap = len(a & b)
    return round(overlap / len(a), 2)


@app.post("/verify")
def verify(data: Input):
    answer = generate_answer(data.question)
    evidence = get_evidence(data.question)
    score = compute_score(answer, evidence)

    if score > 0.6:
        verdict = "Factual"
    elif score > 0.3:
        verdict = "Uncertain"
    else:
        verdict = "Hallucinated"

    return {
        "question": data.question,
        "answer": answer,
        "evidence": evidence,
        "score": score,
        "verdict": verdict
    }
