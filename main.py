import streamlit as st
import openai

# Access the OpenAI API key securely
api_key = st.secrets["OPENAI_API_KEY"]

# Create an OpenAI client using the new SDK style
client = openai.OpenAI(api_key=api_key)

st.set_page_config(page_title="Simple GPT-4o-mini Chatbot", page_icon="💬")

st.title("💬 Simple GPT-4o-mini Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful but simple chatbot."}
    ]

# Display previous messages
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
if user_input := st.chat_input("Say something..."):
    # Add user input to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate assistant response
    with st.chat_message("assistant"):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=st.session_state.messages
        )
        reply = response.choices[0].message.content
        st.markdown(reply)

    # Save assistant response
    st.session_state.messages.append({"role": "assistant", "content": reply})
