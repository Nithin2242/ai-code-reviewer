import streamlit as st
import requests
import json

# --- Page Config ---
st.set_page_config(
    page_title="AI Code Reviewer",
    page_icon="🤖",
    layout="centered"
)

# --- Header ---
st.title("🤖 AI Code Reviewer")
st.markdown("### Paste your buggy code below, and the AI will fix it.")

# --- Input Area ---
code_input = st.text_area(
    "Enter Code:", 
    height=200, 
    placeholder="def my_function()\n    print('Hello World'"
)

# --- The "Review" Button ---
if st.button("Analyze & Fix 🛠️"):
    if not code_input:
        st.warning("Please enter some code first!")
    else:
        with st.spinner("AI is analyzing your logic..."):
            try:
                # 1. Prepare the data
                url = "http://127.0.0.1:5001/review"
                payload = {"code": code_input}
                
                # 2. Send to your Backend (The Waiter)
                response = requests.post(url, json=payload)
                
                # 3. Display Result
                if response.status_code == 200:
                    data = response.json()
                    st.success("Analysis Complete!")
                    
                    st.markdown("### 🔍 AI Feedback:")
                    st.markdown(data['review'])
                else:
                    st.error(f"Server Error: {response.status_code}")
            
            except Exception as e:
                st.error(f"Connection Failed! Is 'server.py' running?\nError: {e}")

# --- Footer ---
st.markdown("---")
st.caption("Powered by Google Gemini 2.5 • Built by Nithin N S")