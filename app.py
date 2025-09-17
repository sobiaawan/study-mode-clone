import streamlit as st
from google import generativeai as genai

# Configure Gemini API key
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

st.set_page_config(page_title="AI Study Mode Clone", layout="wide")
st.title("AI Study Mode Clone 🚀")
st.write("Learn smarter with Explain → Quiz → Review workflow!")

# Sidebar: choose model and stage
model_choice = st.sidebar.selectbox("Choose Gemini Model", ["text-bison-001-flash", "text-bison-001-pro"])
stage = st.sidebar.radio("Select Stage", ["Explain", "Quiz", "Review"])

# User input
topic = st.text_input("Enter a topic or question:")

if st.button("Generate"):
    if topic.strip() == "":
        st.warning("Please enter a topic or question!")
    else:
        st.info("Sending request to Gemini API...")
        try:
            # Construct prompt based on stage
            if stage == "Explain":
                prompt = f"Explain the topic '{topic}' in simple words, step by step."
            elif stage == "Quiz":
                prompt = f"Create 3-5 multiple choice questions on '{topic}' with correct answers."
            elif stage == "Review":
                prompt = f"Give a short summary and key points to remember about '{topic}'."

            # Generate text using Gemini API
            response = genai.models.generate_content(
                model=model_choice,
                contents=prompt,
                max_output_tokens=500
            )

            # Show response
            st.success(f"{stage} Output:")
            st.write(response.text)

        except Exception as e:
            st.error(f"Error: {e}")
            st.write("Check your API key, model name, and project permissions in Google AI Studio.")
