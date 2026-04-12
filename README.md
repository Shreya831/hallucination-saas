# 🚀 TruthGuard AI – LLM Hallucination Detection API

An AI-powered SaaS that detects hallucinations in Large Language Model (LLM) outputs by verifying answers against external knowledge sources.

---

## 💡 Overview

Large Language Models can generate confident but incorrect answers (hallucinations).

TruthGuard AI solves this by using a **multi-agent system**:

* 🤖 Answer Agent → Takes user input
* 🔍 Research Agent → Fetches external evidence
* ⚖️ Judge Agent → Compares using semantic similarity

---

## ⚙️ Features

* Detect hallucinated AI responses
* Semantic similarity scoring
* External evidence retrieval
* FastAPI-based API
* SaaS-ready backend

---

## 🧠 How It Works

1. User submits:

   * Question
   * AI-generated answer

2. System retrieves evidence from web sources

3. Computes similarity between:

   * Answer
   * Evidence

4. Returns:

   * Similarity score
   * Verdict (Factual / Uncertain / Hallucinated)

---

## 📡 API Usage

### Endpoint

```
POST /verify
```

### Request Body

```json
{
  "question": "Who discovered penicillin?",
  "answer": "Alexander Fleming"
}
```

### Response

```json
{
  "answer": "Alexander Fleming",
  "evidence": "Alexander Fleming discovered penicillin...",
  "score": 0.72,
  "verdict": "Factual"
}
```

---

## 🛠️ Tech Stack

* Python
* FastAPI
* Sentence Transformers
* Transformers
* Requests

---

## 🚀 Deployment

Deployed on Render.

---

## 🔮 Future Improvements

* Multi-source verification (Google, PDFs)
* RAG-based architecture
* API key system
* SaaS dashboard

---

## 🙌 Author

Built as part of an AI SaaS project to make LLM outputs more trustworthy.

---
