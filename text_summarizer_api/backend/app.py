from fastapi import FastAPI
from backend.summarizer.pipeline import summarize_text
from backend.models import TextPayload
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500", 
                   "http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Text Summarization API!"}

@app.get("/health")
def health_check():
    return {"status": "OK"}

@app.post("/summarize")
def summarize(payload: TextPayload):
    summary = summarize_text(payload.text)
    return {"summary": summary}