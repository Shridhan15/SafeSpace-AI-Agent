import streamlit as st

st.set_page_config(
    page_title="AI Mental Health Therapist",
    layout="wide",)

st.title("SafeSpace AI Mental Health Therapist")

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []


user_input = st.chat_input("What's on your mind today?")
if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    fixed_response = "I'm here to listen. Can you tell me more about that?"
    st.session_state.chat_history.append({"role": "assistant", "content": fixed_response})

for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])