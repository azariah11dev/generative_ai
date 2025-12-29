import pytest
from fastapi.testclient import TestClient
from backend.app import app

client = TestClient(app)

# ----------- Test: Welcome Message Endpoint -----------
def test_welcome_message():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Text Summarization API!"}

# ----------- Test: Health Check EndPoint -----------
def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}

# ----------- Test: Summarizer (short Text) -----------
def test_summarizer_small_model():
    payload = {"text": "FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints."}
    response = client.post("/summarize", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert len(data["summary"]) > 0

# ----------- Test: Summarizer (medium Text) -----------
def test_summarizer_medium_model():
    text = "word" * 400 # Simulating a medium text by repeating a word
    payload = {"text": text}
    response = client.post("/summarize", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert len(data["summary"]) > 0

# ----------- Test: Summarizer (long Text) -----------
def test_summarizer_large_model():
    text = "word" * 2000 # Simulating a long text by repeating a word
    payload = {"text": text}
    response = client.post("/summarize", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    assert len(data["summary"]) > 0

# ----------- Nonsense Input Handling -----------
def test_summarizer_nonsense_input():
    payload = {"text": "13534535@#$#$^^^$#@QWR@% I ate 4567 bananas!!! your life 999 is 00000 great ###@"}
    response = client.post("/summarize", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert len(data["summary"]) > 0
    assert isinstance(data["summary"], str)
