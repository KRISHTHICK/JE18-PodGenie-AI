import streamlit as st
from rag_script_gen import generate_script
from ai_hosts import simulate_conversation
from utils.file_loader import extract_text

st.set_page_config(page_title="🎙️ PodGenie AI", layout="centered")
st.title("🎙️ PodGenie AI – Generate Podcast Scripts from Blogs or News")

file = st.file_uploader("📄 Upload blog/news (PDF or TXT)", type=["pdf", "txt"])
mode = st.radio("Choose Mode", ["🎤 Solo Host", "👥 Host-Guest Duo"])
style = st.selectbox("Script Style", ["Conversational", "Formal", "Humorous"])

if file:
    text = extract_text(file)
    if mode == "🎤 Solo Host":
        script = generate_script(text, style)
    else:
        script = simulate_conversation(text)

    st.subheader("🎧 Podcast Script")
    st.text_area("Script Preview", script, height=400)

    st.download_button("📥 Download Script", script, file_name="podcast_script.txt")
