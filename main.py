import streamlit as st
import openai
import os

# Set your OpenAI API key (safe method)
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="Simple GPT-4o-mini Chatbot", page_icon="💬")

st.title("💬 Simple GPT-4o-mini Chatbot")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful but simple chatbot."}
    ]

# Display chat history
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
if user_input := st.chat_input("Say something..."):
    # Add user message to session state
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Call OpenAI API
    with st.chat_message("assistant"):
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=st.session_state.messages,
        )
        reply = response.choices[0].message["content"]
        st.markdown(reply)

    # Save assistant reply
    st.session_state.messages.append({"role": "assistant", "content": reply})
