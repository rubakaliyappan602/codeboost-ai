
import streamlit as st
from groq import Groq

# Create Groq client
client = Groq(api_key="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")

# Page settings
st.set_page_config(page_title="CodeBoost AI", page_icon="🤖")

st.title("CodeBoost AI - Developer Sidekick")

# Feature selector
feature = st.selectbox(
    "Select Feature",
    [
        "Code Generator",
        "Explain Code",
        "Debug Error",
        "Generate Tests"
    ]
)

# User input
user_input = st.text_area("Enter your prompt or code")

# Function to call AI
def ask_ai(prompt):
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

# Run button
if st.button("Run AI"):

    if user_input.strip() == "":
        st.warning("Please enter a prompt or code.")
    else:

        if feature == "Code Generator":
            prompt = f"Generate code for the following request:\n{user_input}"

        elif feature == "Explain Code":
            prompt = f"Explain this code in simple terms:\n{user_input}"

        elif feature == "Debug Error":
            prompt = f"Fix the bug in this code and explain the fix:\n{user_input}"

        elif feature == "Generate Tests":
            prompt = f"Generate unit tests for the following code:\n{user_input}"

        result = ask_ai(prompt)

        st.subheader("AI Response")
        st.write(result)
