from transformers import pipeline

summarizer = pipeline("summarization")

text = """
India is a country in South Asia. It is the seventh-largest country by area, 
the most populous country as of 2023, and the most populous democracy in the world. 
Bounded by the Indian Ocean on the south, the Arabian Sea on the southwest, 
and the Bay of Bengal on the southeast, it shares land borders with Pakistan to the west, 
China, Nepal, and Bhutan to the north; and Bangladesh and Myanmar to the east.
"""

summary = summarizer(text, max_length=50, min_length=25, do_sample=False)

print("\n--- Summary ---\n", summary[0]['summary_text'])


