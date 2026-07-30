import streamlit as st

from services.pdf_reader import extract_text
from ui.reading import render_reading
from ui.quiz import render_quiz

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

    if st.session_state.get("uploaded_file_name") != uploaded_file.name:
        st.session_state.clear()
        st.session_state["uploaded_file_name"] = uploaded_file.name

    try:
        pdf_bytes = uploaded_file.read()
        text = extract_text(pdf_bytes)
    except Exception as error:
        st.error(f"Couldn't read this PDF: {error}")
        return

    if not text.strip():
        st.error("Couldn't find any text in this PDF. It might be a scanned image — try a different file.")
        return

    st.success(f"{uploaded_file.name} loaded successfully!")

    st.subheader("What would you like to do?")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🎧 Listen to my notes", use_container_width=True):
            st.session_state["mode"] = "reading"

    with col2:
        if st.button("🧠 Practice for exam", use_container_width=True):
            st.session_state["mode"] = "quiz"

    if st.session_state.get("mode") == "reading":
        render_reading(text)
    elif st.session_state.get("mode") == "quiz":
        render_quiz(text)