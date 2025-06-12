from transformers import pipeline

# Summarizer pipeline
summarizer = pipeline("summarization")

# ✅ మీరు summarize చేయాలనుకునే text
text = """
My name is Deva, and I am currently in the final year of my B.Tech in Mechanical Engineering.
Over the past three years, I have developed a strong foundation in mechanical concepts like thermodynamics,
fluid mechanics, machine design, and manufacturing processes. I have also completed internships in reputed companies
where I gained hands-on experience with industry-level machines and CAD tools. In my spare time, I enjoy learning new
technologies, especially in AI and automation, as I believe they play a crucial role in the future of mechanical systems.
My goal is to combine my mechanical engineering background with modern technologies to innovate and contribute to the industry.
"""

# Summary generate చేయండి
summary = summarizer(text, max_length=60, min_length=25, do_sample=False)

# Output చూపించండి
print("\n--- Summary ---\n", summary[0]['summary_text'])

