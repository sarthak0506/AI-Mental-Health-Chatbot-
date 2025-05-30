import streamlit as st
import os, time, datetime
from dotenv import load_dotenv
from langchain_together import Together
from langchain.llms import Cohere
import pickle, json

# ─── Load Your Trained Model & Vectorizer ───
with open("chatbot_model.pkl", "rb") as f:
    model = pickle.load(f)
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

load_dotenv()
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

# ─── Predefined Mental Health Dataset ───
def load_mental_health_data():
    return {
        "anxiety": "Try deep breathing exercises to calm your mind.",
        "stress": "Take a short walk outside to refresh yourself.",
        "depressed": "Reach out to friends or a professional. Small steps help.",
        "overwhelmed": "Break tasks into small steps. Focus on one at a time.",
        "sad": "Listen to uplifting music or journal your thoughts."
    }

# ─── AI Models ───
models = {
    "LLaMA 3.3 Turbo": Together(
        model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
        together_api_key=TOGETHER_API_KEY
    ),
    "LLaMA Vision": Together(
        model="meta-llama/Llama-Vision-Free",
        together_api_key=TOGETHER_API_KEY
    ),
    "ChatBot": Cohere(
        model="command-xlarge",
        cohere_api_key=COHERE_API_KEY
    )
}

# ─── Prompt Template ───
SYSTEM_PROMPT = """
You are a kind and supportive mental health assistant.
Respond in 3-4 lines with positive and practical advice.
Be warm, empathetic, and provide calming, actionable suggestions.
"""

def get_response(model_name, user_query):
    for keyword, advice in load_mental_health_data().items():
        if keyword in user_query.lower():
            user_query += f"\n[Note: {advice}]"
    prompt = SYSTEM_PROMPT + "\nUser: " + user_query + "\nAI:"
    try:
        response = models[model_name].invoke(prompt, max_tokens=100).strip()
        return response
    except Exception as e:
        return f"⚠️ Error: {e}"

#  Streamlit
st.set_page_config(page_title="Mental Health Chatbot", layout="wide")

# Title
st.markdown("<h1 style='text-align: center; color: #00e676;'>💬 Mental Health Chatbot</h1>", unsafe_allow_html=True)
st.write("🌿 A calming AI companion for your mental well-being.")

st.markdown("""
<style>
.chat-message { padding:12px; border-radius:8px; margin:10px 0; font-size:16px; }
.user-message { background:linear-gradient(135deg,#007aff,#00c6ff); color:#fff; text-align:right; }
.ai-message   { background:linear-gradient(135deg,#00e676,#1de9b6); color:#000; text-align:left; }
</style>
""", unsafe_allow_html=True)

# ─── Session Init ───
if "messages" not in st.session_state:
    st.session_state.messages = [
        ("ai-message", "<strong>Chatbot:</strong> Hello! How are you feeling today?", datetime.datetime.now().strftime("%H:%M:%S"))
    ]

# Model Selection
#model_choice = st.selectbox("🛠 Select AI Model:", list(models.keys()))
# Add this fixed model choice
model_choice = "ChatBot"
# ─── Chat Display ───
for role, text, ts in st.session_state.messages:
    st.markdown(
        f"<div class='chat-message {role}'>{text}<br><small style='color:gray;'>🕒 {ts}</small></div>",
        unsafe_allow_html=True
    )


with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("💬 Type your message here...")
    submitted = st.form_submit_button("Send")

# ─── Handle Send ───
if submitted:
    if user_input.strip():
        now = datetime.datetime.now().strftime("%H:%M:%S")
        st.session_state.messages.append(("user-message", f"<strong>You:</strong> {user_input}", now))
        with st.spinner("AI is typing..."):
            time.sleep(1)
            reply = get_response(model_choice, user_input)
        now = datetime.datetime.now().strftime("%H:%M:%S")
        st.session_state.messages.append(("ai-message", f"<strong>{model_choice}:</strong> {reply}", now))
        st.rerun()
    else:
        st.warning("⚠️ Please type a message before sending.")

# ─── Clear Chat Button ───
if st.button("🗑 Clear Chat"):
    st.session_state.messages = []
    st.rerun()