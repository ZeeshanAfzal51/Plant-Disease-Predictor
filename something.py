import streamlit as st
import datetime

# Encryption and Decryption Functions
def encrypt(text):
    return ''.join(chr(ord(c) + 5) for c in text)

def decrypt(text):
    return ''.join(chr(ord(c) - 5) for c in text)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []
if "show_decrypted" not in st.session_state:
    st.session_state["show_decrypted"] = False

st.title("Encrypted Chat Room")

# Display messages
for msg in st.session_state["messages"]:
    text = decrypt(msg["text"]) if st.session_state["show_decrypted"] else msg["text"]
    st.write(f"{msg['timestamp']}: {text}")

# Toggle deciphering
if st.button("Toggle Decipher Text"):
    st.session_state["show_decrypted"] = not st.session_state["show_decrypted"]
    st.experimental_rerun()

# Input field
new_message = st.text_input("Type your message...")
if st.button("Send") and new_message.strip():
    encrypted_message = encrypt(new_message)
    st.session_state["messages"].append({
        "text": encrypted_message,
        "timestamp": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })
    st.experimental_rerun()
