import streamlit as st
from groq import Groq

# Page title
st.title("CodeBoost AI - Developer Sidekick")

# Load API key from Streamlit secrets
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Feature selection
feature = st.selectbox("Select Feature", ["Code Generator"])

# Prompt input
prompt = st.text_area("Enter your prompt or code")

# Function to ask AI
def ask_ai(prompt):
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


# Run button
if st.button("Run AI"):

    if prompt.strip() == "":
        st.warning("Please enter a prompt")

    else:
        result = ask_ai(prompt)
        st.code(result)
