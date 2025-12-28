from transformers import pipeline

#Load a lightweight summarization model
summarizer = pipeline(
    "summarization", model="sshleifer/distilbart-cnn-12-6"
    )

def summarize_text(text: str) -> str:
    result = summarizer(
        text,
        max_length = 120,
        min_length = 40,
        do_sample = False
        )
    return result[0]['summary_text']