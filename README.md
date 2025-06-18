# JE18-PodGenie-AI
Gen Ai

🎙️📻 PodGenie AI – Podcast Episode Generator from Blogs & News using RAG + Ollama
💡 Project Idea:
PodGenie AI transforms blogs, news articles, or user PDFs into short, engaging podcast scripts or spoken summaries. It uses RAG to ground the generation on uploaded content and Ollama LLM to rewrite the information in a conversational podcast tone.

You can even simulate a 2-host conversation (e.g., Host-AI and Guest-AI), and optionally download the script or connect it to a TTS (text-to-speech) engine for audio generation.

🌟 Key Features:
Feature	Description
📰 Upload Blog/News as Input	Upload .txt, .pdf, or URL of a blog or news
🧠 RAG-Based Summarizer	Uses document content to ground the generation
🎤 Podcast Script Generator	Generates natural, engaging scripts in podcast style
🧑‍🤝‍🧑 2-AI Host Mode	Simulates a conversation between host and guest AI
🔄 Rephrase/Shorten Options	Allows switching style (formal, humorous, bullet points)
📁 Download Script Button	Save final podcast script as .txt
🔊 (Optional) Text-to-Speech Hook	Future add-on: convert script into voice

🚀 To Run
'''bash
Copy
Edit
pip install -r requirements.txt
ollama run tinyllama
streamlit run app.py
