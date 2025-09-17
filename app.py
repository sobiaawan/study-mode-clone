import streamlit as st
from google import generativeai as genai

# Load API key from Streamlit secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Ask user for topic
topic = st.text_input("Enter topic:")

if st.button("Generate"):
    if topic:
        try:
            # Use generate_content() instead of generate_text()
            response = genai.generate_content(
                model="text-bison-001-flash",   # or "text-bison-001-pro"
                contents=f"Explain the topic '{topic}' in simple words",
                max_output_tokens=500
            )
            # Show the generated text
            st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")


