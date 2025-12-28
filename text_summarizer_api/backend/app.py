from fastapi import FastAPI
from summarizer.pipeline import summarize_text
from models import TextPayload

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Text Summarization API!"}

@app.post("/summarize")
def summarize(payload: TextPayload):
    summary = summarize_text(payload.text)
    return {"summary": summary}