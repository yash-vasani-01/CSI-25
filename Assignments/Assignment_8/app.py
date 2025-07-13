
import streamlit as st
from rag import create_chat_chain

st.set_page_config("Loan RAG Chatbot", layout="wide")

st.markdown("""
<style>
    body {
        background-color: #ffffff;
    }
    .stChatMessage {
        margin: 10px 0;
        padding: 10px 20px;
        border-radius: 10px;
    }
    .stChatMessage.user {
        background-color: #dcf8c6;
        text-align: left;
    }
    .stChatMessage.assistant {
        background-color: #f1f0f0;
        text-align: left;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>📊 Loan Eligibility Chatbot</h1>", unsafe_allow_html=True)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "chat_chain" not in st.session_state:
    st.session_state.chat_chain = create_chat_chain()


query = st.chat_input("Ask about loans, approvals, or applicants...")

if query:
    response = st.session_state.chat_chain.invoke({
        "question": query,
        "chat_history": st.session_state.chat_history
    })
    print(response)
    st.session_state.chat_history.append((query, response["answer"]))

for msg in st.session_state.chat_history:
    user_msg, bot_msg = msg
    with st.chat_message("user"):
        st.markdown(user_msg)
    with st.chat_message("assistant"):
        st.markdown(bot_msg)
