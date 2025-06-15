import streamlit as st
from summarizer import summarize_text
import PyPDF2
import io

st.set_page_config(page_title="తెలుగు టెక్స్ట్ సమ్మరైజర్", layout="centered")
st.title("📄 టెక్స్ట్ సమ్మరైజర్ టూల్")

with st.sidebar:
    st.header("⚙️ కంట్రోల్‌లు")
    length = st.selectbox("సమ్మరీ పొడవు ఎంచుకోండి:", ["చిన్నదిగా", "మధ్యస్థంగా", "పొడవుగా"])
    if length == "చిన్నదిగా":
        min_len, max_len = 20, 50
    elif length == "మధ్యస్థంగా":
        min_len, max_len = 50, 120
    else:
        min_len, max_len = 120, 200

    uploaded_file = st.file_uploader("📁 PDF ఫైల్ ఎంచుకోండి", type=["pdf"])

text_input = ""

if uploaded_file:
    reader = PyPDF2.PdfReader(uploaded_file)
    for page in reader.pages:
        text_input += page.extract_text()
else:
    text_input = st.text_area("✍️ మీరు సమ్మరైజ్ చేయాలనుకుంటున్న టెక్స్ట్ ను ఇక్కడ రాయండి:")

if st.button("📌 సమ్మరైజ్ చేయండి"):
    with st.spinner("సమ్మరీ తయారవుతోంది..."):
        summary = summarize_text(text_input, min_length=min_len, max_length=max_len)
        st.subheader("🧠 సమ్మరీ ఫలితం:")
        st.success(summary)

        # Download link
        st.download_button("⬇️ సమ్మరీ డౌన్లోడ్ చేయండి", summary, file_name="summary.txt")

