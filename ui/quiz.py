import json

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
- For each question, also provide a concise reference answer.
- Write the questions and answers in a clear and concise way.

Lecture notes:
{lecture_notes}
"""

QUIZ_SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "question": {"type": "string"},
            "answer": {"type": "string"},
        },
        "required": ["question", "answer"],
    },
}

def generate_quiz(notes):
    prompt = QUIZ_PROMPT.format(lecture_notes=notes)
    response = ask_llm(prompt, response_schema=QUIZ_SCHEMA)
    return json.loads(response)

def render_quiz(notes: str):

    if st.session_state.get("quiz_source") != notes:
        try:
            with st.spinner("Generating quiz..."):
                quiz = generate_quiz(notes)
        except Exception as error:
            st.error(f"Couldn't generate the quiz: {error}")
            return

        st.session_state["quiz"] = quiz
        st.session_state["quiz_source"] = notes

    for i, item in enumerate(st.session_state["quiz"], start=1):
        st.markdown(f"**{i}. {item['question']}**")
        with st.expander("Show answer"):
            st.write(item["answer"])