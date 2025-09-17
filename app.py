import streamlit as st
import os
import google.generativeai as genai

# Configure Gemini with your API key from secrets
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

st.title("Study Mode Clone 📚")

# User input
user_input = st.text_input("Ask me anything:")

if user_input:
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(user_input)

    st.write("**Answer:**")
    st.write(response.text)


