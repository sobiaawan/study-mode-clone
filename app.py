import streamlit as st
from google import generativeai as genai

# Configure Gemini API key
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

st.title("AI Study Mode Clone")
st.write("Learn smarter with Explain → Quiz → Review workflow!")

# Sidebar: choose model
model_choice = st.sidebar.selectbox("Choose Gemini Model", ["text-bison-001-flash", "text-bison-001-pro"])

# Sidebar: choose stage
stage = st.sidebar.radio("Select Stage", ["Explain", "Quiz", "Review"])

# User input topic
topic = st.text_input("Enter a topic or question:")

if st.button("Generate"):
    if topic.strip() == "":
        st.warning("Please enter a topic or question!")
    else:
        try:
            prompt = ""
            
            if stage == "Explain":
                prompt = f"Explain the topic '{topic}' in simple words, step by step."
            elif stage == "Quiz":
                prompt = f"Create 3-5 multiple choice questions on '{topic}' with correct answers."
            elif stage == "Review":
                prompt = f"Give a short summary and key points to remember about '{topic}'."
            
            response = genai.generate_text(
                model=model_choice,
                prompt=prompt,
                max_output_tokens=500
            )
            
            st.subheader(f"{stage} Output:")
            st.write(response.text)
            
        except Exception as e:
            st.error(f"Error: {e}")






