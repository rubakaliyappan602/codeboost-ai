import streamlit as st
import openai

# Put your OpenAI API key here
openai.api_key = "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"

st.title("CodeBoost AI - Developer Sidekick")

feature = st.selectbox(
    "Select Feature",
    ["Code Generator", "Error Explainer", "Code Explanation", "Documentation Generator"]
)

user_input = st.text_area("Enter your prompt or code")

def ask_ai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"]

if st.button("Run AI"):

    if feature == "Code Generator":
        prompt = f"Generate working code for: {user_input}"

    elif feature == "Error Explainer":
        prompt = f"Explain this programming error and give solution: {user_input}"

    elif feature == "Code Explanation":
        prompt = f"Explain this code line by line: {user_input}"

    elif feature == "Documentation Generator":
        prompt = f"Add comments and documentation to this code: {user_input}"

    result = ask_ai(prompt)

    st.subheader("AI Output")
    st.write(result)
