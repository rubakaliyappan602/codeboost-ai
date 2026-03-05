import streamlit as st
from groq import Groq

st.set_page_config(page_title="CodeBoost AI", layout="wide")

st.title("CodeBoost AI - Developer Sidekick")

# Feature dropdown
feature = st.selectbox(
    "Select Feature",
    ["Code Generator", "Bug Fixer", "Code Explainer"]
)

# User input
prompt = st.text_area("Enter your prompt or code")

# Check API key
if "GROQ_API_KEY" not in st.secrets:
    st.error("Groq API Key not found. Please add it in Streamlit Secrets.")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])


def ask_ai(user_prompt):
    try:
        response = client.chat.completions.create(
           model="llama-3.1-8b-instant",
            messages=[
                {"role": "user", "content": user_prompt}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {e}"


# Run button
if st.button("Run AI"):

    if prompt.strip() == "":
        st.warning("Please enter a prompt.")

    else:
        with st.spinner("Generating response..."):
            result = ask_ai(prompt)

        st.subheader("AI Response")
        st.write(result)
