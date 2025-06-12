from transformers import pipeline

# Model load once
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text, length="medium"):
    if length == "short":
        max_len, min_len = 50, 25
    elif length == "long":
        max_len, min_len = 250, 150
    else:  # default = medium
        max_len, min_len = 120, 60

    summary = summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)[0]['summary_text']
    return summary


