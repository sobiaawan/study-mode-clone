import streamlit as st
import os
import google.generativeai as genai

# Configure Gemini with your API key from secrets
genai.configure(api_key=os.environ["AIzaSyBlq6_yZZgQUJHR6i97T-bflcggVLZbQkE"])

st.title("Study Mode Clone 📚")

# User input
user_input = st.text_input("Ask me anything:")

if user_input:
    model = genai.GenerativeModel("gemini 1.5 flash")
    response = model.generate_content(user_input)

    st.write("**Answer:**")



