import streamlit as st
import google.generativeai as genai

# --- Page Config (Browser Tab & Wide Mode) ---
st.set_page_config(
    page_title="AI Code Reviewer",
    page_icon="⚡",
    layout="wide", # This enables the full-width view
    initial_sidebar_state="expanded"
)

# --- Custom Styles (CSS) to make it look cleaner ---
st.markdown("""
    <style>
    .main {
        background-color: #0E1117;
    }
    .stTextArea textarea {
        background-color: #1E1E1E;
        color: #00FF99; /* Hacker Green Text */
        font-family: 'Courier New', monospace;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Sidebar (Settings & Info) ---
with st.sidebar:
    st.title("⚡ AI Reviewer")
    st.markdown("Your personal **AI Pair Programmer**.")
    st.divider()
    
    st.info("💡 **Tip:** Paste your entire function or class for the best results.")
    
    st.markdown("---")
    st.caption("Built by **Nithin N S**")
    st.caption("Powered by **Gemini 2.5**")

# --- API Key Handling ---
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
except:
    st.error("⚠️ API Key missing! Add it in Streamlit Secrets.")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.5-flash')

# --- Main Layout (Two Columns) ---
st.title("🛠️ AI Code Fixer & Optimizer")
st.markdown("Debug your code instantly. Compare **Your Code** (Left) vs **Fixed Code** (Right).")

# Create two columns: Col 1 for Input, Col 2 for Output
col1, col2 = st.columns([1, 1], gap="medium")

with col1:
    st.subheader("📝 Your Buggy Code")
    code_input = st.text_area(
        "Paste code here:", 
        height=500, # Taller box
        placeholder="def my_function():\n    print('Hello World'",
        label_visibility="collapsed"
    )

with col2:
    st.subheader("✨ AI Fixed Code")
    # We use a container to hold the output so it aligns nicely
    output_container = st.container()

# --- The Logic ---
if st.button("🚀 Analyze & Fix Code", type="primary", use_container_width=True):
    if not code_input:
        st.warning("⚠️ Please enter some code first!")
    else:
        with output_container:
            with st.spinner("🤖 AI is reading your code..."):
                try:
                    # Prompt Engineering
                    prompt = f"""
                    Act as a Senior Software Engineer. 
                    1. Review the code below.
                    2. FIXED CODE: Provide the corrected code in a code block.
                    3. EXPLANATION: Explain briefly what was wrong (bullet points).
                    
                    Code:
                    {code_input}
                    """
                    
                    response = model.generate_content(prompt)
                    
                    # Display Result
                    st.success("Analysis Complete!")
                    st.markdown(response.text)
                    
                except Exception as e:
                    st.error(f"Error: {e}")