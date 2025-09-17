import streamlit as st

# Title of the app
st.title("ChatGPT Study Mode Clone")

# Description
st.write("Hello! This is your Study Mode app.")

# Ask user for a topic
topic = st.text_input("Enter a topic to study:")

# Button to start learning
if st.button("Start Learning"):
    if topic:
        st.write(f"Studying topic: {topic}")
    else:
        st.write("Please enter a topic first!")
