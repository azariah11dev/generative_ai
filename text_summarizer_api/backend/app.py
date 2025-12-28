from fastapi import FastAPI
from backend.summarizer.pipeline import summarize_text
from backend.models import TextPayload

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Text Summarization API!"}

@app.post("/summarize")
def summarize(payload: TextPayload):
    summary = summarize_text(payload.text)
    return {"summary": summary}