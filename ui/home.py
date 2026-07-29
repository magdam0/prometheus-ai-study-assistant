import streamlit as st

from services.pdf_reader import extract_text


def render_homepage():
    st.title("🎓 AI Study Assistant")

    uploaded_file = st.file_uploader(
        "Upload your lecture notes",
        type=["pdf"]
    )

    if uploaded_file:
        pdf_bytes = uploaded_file.read()
        text = extract_text(pdf_bytes)

        st.success("PDF loaded!")

        st.text_area(
            "Extracted text",
            text,
            height=400
        )