import streamlit as st
import openai

# Direct API key (for local testing only)
openai.api_key = "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"

# Create OpenAI client
client = openai.OpenAI(api_key=openai.api_key)

st.set_page_config(page_title="Simple GPT-4o-mini Chatbot", page_icon="💬")
st.title("💬 Simple GPT-4o-mini Chatbot")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a simple and helpful chatbot."}
    ]

# Display past messages
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Get user input
if user_input := st.chat_input("Say something..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Use new SDK method
    with st.chat_message("assistant"):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=st.session_state.messages
        )
        reply = response.choices[0].message.content
        st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
