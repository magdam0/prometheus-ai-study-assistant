import streamlit as st

from services.pdf_reader import extract_text
from ui.reading import render_reading

def render_homepage():

    st.title("🎓 AI Study Assistant")

    st.subheader("Upload your lecture notes:")

    uploaded_file = st.file_uploader(
        "Lecture notes file",
        type=["pdf"],
        label_visibility="collapsed"
    )

    if not uploaded_file:
        return

    pdf_bytes = uploaded_file.read()
    text = extract_text(pdf_bytes)

    st.success(f"{uploaded_file.name} loaded successfully!")

    st.subheader("What would you like to do?")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🎧 Listen to my notes", use_container_width=True):
            render_reading(text)

    with col2:
        if st.button("🧠 Practice for exam", use_container_width=True):
            render_quiz(text)