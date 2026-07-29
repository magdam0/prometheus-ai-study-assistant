import streamlit as st

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 AI Study Assistant")

uploaded_file = st.file_uploader(     
    "Upload your lecture notes",     
    type=["pdf"] 
)