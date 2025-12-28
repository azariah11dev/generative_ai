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

"""
# Check device (CPU/GPU) being used by the model
# for testing purposes only
# remove # from print function and run this file directly to see the device info
"""
# print(f"{summarizer.model.device}")