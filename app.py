import streamlit as st
from google import generativeai as genai

# Configure Gemini API key from Streamlit secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

st.title("AI Study Mode Clone")

# Sidebar to choose model
model_choice = st.sidebar.selectbox("Choose Gemini Model", ["text-bison-001-flash", "text-bison-001-pro"])

# User input
user_input = st.text_area("Enter your question or topic:")

if st.button("Generate Answer"):
    if user_input.strip() == "":
        st.warning("Please enter some text!")
    else:
        try:
            # Call Gemini API
            response = genai.generate_text(
                model=model_choice,
                prompt=user_input,
                max_output_tokens=300
            )
            st.subheader("Answer:")
            st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")




