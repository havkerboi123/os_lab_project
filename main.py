import streamlit as st
import subprocess

# Streamlit UI
st.title("ChatGPT-like Chatbot")
st.write("A simple UI for your chatbot using Streamlit 🚀")

# Text input for user message
user_input = st.text_input("Enter your message:", key="input")

# Function to call the shell script
def call_shell_script(user_message):
    try:
        # Run the shell script and pass user input
        result = subprocess.run(
            ["/bin/bash", "/Users/mhmh/Desktop/data/d2/script.sh"],
            input=user_message,
            text=True,
            capture_output=True
        )
        return result.stdout.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Display chatbot response
if st.button("Send"):
    if user_input:
        response = call_shell_script(user_input)
        st.text_area("Chatbot Response:", response, height=150)
    else:
        st.warning("Please enter a message to send!")

# Option to exit
if st.button("Exit"):
    st.stop()
