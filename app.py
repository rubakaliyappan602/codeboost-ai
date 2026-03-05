
import streamlit as st
from groq import Groq

# Page title
st.title("CodeBoost AI - Developer Sidekick")

# Dropdown
feature = st.selectbox(
    "Select Feature",
    ["Code Generator", "Bug Fixer", "Code Explainer"]
)

# User input
prompt = st.text_area("Enter your prompt or code")

# Load API key
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Function to call AI
def ask_ai(user_prompt):

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "user", "content": user_prompt}
        ]
    )

    return response.choices[0].message.content


# Run button
if st.button("Run AI"):

    if prompt.strip() == "":
        st.warning("Please enter a prompt.")
    else:
        result = ask_ai(prompt)
        st.subheader("AI Response")
        st.write(result)
