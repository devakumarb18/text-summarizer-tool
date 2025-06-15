from transformers import pipeline

# Default summarizer
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text, max_length=130, min_length=30):
    if not text.strip():
        return "దయచేసి సరైన టెక్స్ట్ ఇవ్వండి."
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']


