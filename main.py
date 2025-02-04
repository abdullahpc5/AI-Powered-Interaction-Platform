import streamlit as st
import openai 

# Set up the page
st.set_page_config(page_title="AI Chat Interface", layout="centered")

st.title("AI-Powered Interaction Platform")
st.write("Experience seamless interactions with Llama 3, powered by NVIDIA’s cutting-edge AI.")

# User input
prompt = st.text_area("Enter your prompt:", "")

# API Key input
api_key = "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"

# Function to fetch AI-generated response
def get_ai_response(prompt, api_key):
    client = openai(
        base_url="https://integrate.api.nvidia.com/v1",
        api_key=api_key
    )
    
    completion = client.chat.completions.create(
        model="meta/llama3-8b-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        top_p=1,
        max_tokens=1024,
        stream=True
    )
    
    response_text = ""
    for chunk in completion:
        if chunk.choices[0].delta.content:
            response_text += chunk.choices[0].delta.content
            yield response_text  # Stream output progressively

if st.button("Generate Response"):
    if not api_key:
        st.error("Please enter an API key.")
    else:
        st.subheader("Response:")
        response_container = st.empty()  # Placeholder for streaming response
        
        for response in get_ai_response(prompt, api_key):
            response_container.markdown(f"```\n{response}\n```")  # Stream text

        st.success("Response Generated Successfully.")
