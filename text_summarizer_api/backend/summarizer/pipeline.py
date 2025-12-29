from transformers import pipeline

#Load a lightweight summarization model
summarizer_small = pipeline(
    "summarization", model="sshleifer/distilbart-cnn-12-6"
    )

#Load a medium-sized summarization model
summarizer_medium = pipeline(
    "summarization", model="facebook/bart-large-cnn"
    )

#Load a large-sized summarization model
summarizer_large = pipeline(
    "summarization", model="allenai/led-base-16384"
    )

def summarize_text(text: str) -> str:
    length = len(text)
    if length < 1500:
        result = summarizer_small(
            text,
            max_length = 120,
            min_length = 40,
            do_sample = False
            )
    elif length < 5000 and length >= 1500:
        result = summarizer_medium(
            text,
            max_length = 180,
            min_length = 60,
            do_sample = False
            )
    else:
        result = summarizer_large(
            text,
            max_length = 256,
            min_length = 64,
            do_sample = False
            )
    return result[0]['summary_text']

"""
# Check device (CPU/GPU) being used by the model
# for testing purposes only
# remove # from print function and run this file directly to see the device info
"""
# print(f"{summarizer_small.model.device}")
# print(f"{summarizer_medium.model.device}")
# print(f"{summarizer_large.model.device}")