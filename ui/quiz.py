import streamlit as st

from services.llm import ask_llm

QUIZ_PROMPT = """
You are an experienced university lecturer preparing a student for an exam.

Your task is to generate a quiz based ONLY on the provided lecture notes.

Requirements:
- Create 10 questions of varying difficulty.
- Include a mix of factual, conceptual, and analytical questions where appropriate.
- Cover the most important topics from the lecture notes.
- Do not ask about information that is not present in the notes.
- Do not provide the answers.
- Number the questions clearly.
- Write the questions in a clear and concise way.

Lecture notes:
{lecture_notes}
"""

def generate_quiz(notes):
    prompt = QUIZ_PROMPT.format(lecture_notes=notes)
    return ask_llm(prompt)

def render_quiz(notes: str):

    with st.spinner("Generating quiz..."):
        quiz = generate_quiz(notes)

    st.markdown(quiz)