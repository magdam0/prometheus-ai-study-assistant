import streamlit as st

from services.pdf_reader import extract_text


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

    # mode = st.radio(
    #     "What would you like to do?",
    #     [
    #         "🎧 Listen to my notes",
    #         "🧠 Practice for exam"
    #     ]
    # )

    # if mode == "🎧 Listen to my notes":

    #     if st.button("Generate lesson"):
    #         render_reading(text)

    # else:

    #     if st.button("Start quiz"):
    #         render_quiz(text)
    st.subheader("What would you like to do?")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🎧 Listen to my notes")
        if st.button("Generate lesson", use_container_width=True):
            render_reading(text)

    with col2:
        st.markdown("### 🧠 Practice for exam")
        if st.button("Start quiz", use_container_width=True):
            render_quiz(text)