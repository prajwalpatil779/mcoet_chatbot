import streamlit as st
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
import requests
import json

# ============================================================
# OLLAMA - Free Local AI (no API key needed!)
# ============================================================
OLLAMA_API_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "mistral"

@st.cache_resource
def load_database():
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectordb = Chroma(persist_directory="./college_db", embedding_function=embeddings)
    return vectordb

def query_ollama(prompt):
    """Query Ollama local LLM"""
    try:
        response = requests.post(
            OLLAMA_API_URL,
            json={
                "model": OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False,
                "temperature": 0.7
            },
            timeout=180
        )
        if response.status_code == 200:
            result = response.json()
            return result.get("response", "No response from model")
        else:
            return f"Error: {response.status_code} - Make sure Ollama is running with: ollama serve"
    except requests.exceptions.ConnectionError:
        return "❌ Ollama not running! Start it with: ollama serve"
    except Exception as e:
        return f"Error: {str(e)}"

st.set_page_config(page_title="MCOET Chatbot", page_icon="🎓", layout="centered")

st.markdown("""
    <div style='text-align:center; padding:15px; background-color:#1a3c6b;
                border-radius:10px; margin-bottom:20px'>
        <h2 style='color:white; margin:0'>🎓 MCOET Virtual Assistant</h2>
        <p style='color:#ccc; margin:0'>Mauli College of Engineering and Technology, Shegaon</p>
    </div>
""", unsafe_allow_html=True)

st.write("👋 Hello! Ask me anything about MCOET — admissions, courses, fees, placements, campus and more!")

with st.spinner("Loading college knowledge base..."):
    vectordb = load_database()

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if question := st.chat_input("Type your question here..."):
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):
        with st.spinner("Searching MCOET information..."):
            relevant_docs = vectordb.similarity_search(question, k=5)
            context = "\n\n".join([doc.page_content for doc in relevant_docs])

            prompt = f"""You are a helpful virtual assistant for MCOET (Mauli College of Engineering and Technology, Shegaon).

Your job is to help students, parents and visitors by answering their questions about the college.

IMPORTANT RULES:
1. Answer ONLY from the college information provided below
2. If answer is not found, say: "I don't have that info. Contact MCOET at maulicoet@gmail.com or call 7722027506"
3. Be friendly, clear and helpful
4. Keep answers concise but complete

MCOET COLLEGE INFORMATION:
{context}

STUDENT QUESTION: {question}

HELPFUL ANSWER:"""

            try:
                answer = query_ollama(prompt)
            except Exception as e:
                answer = f"Error: {str(e)}"

        st.write(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})

st.markdown("---")
st.markdown("<p style='text-align:center;color:gray;font-size:12px'>MCOET Chatbot • 📞 7722027506 • maulicoet@gmail.com</p>", unsafe_allow_html=True)
