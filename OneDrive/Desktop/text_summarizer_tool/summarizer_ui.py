import streamlit as st
from summarizer import summarize_text

st.title("🧠 Advanced Text Summarizer")

input_text = st.text_area("📄 Enter text to summarize")

# Summary length selection
length_option = st.selectbox("📏 Choose summary length", ["short", "medium", "long"])

if st.button("Summarize"):
    if input_text.strip() == "":
        st.error("Please enter some text.")
    else:
        summary = summarize_text(input_text, length=length_option)
        st.write("### ✂️ Summary:")
        st.success(summary)
