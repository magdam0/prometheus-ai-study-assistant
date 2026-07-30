import streamlit as st

from services.llm import ask_llm
from services.tts import synthesize_speech

LESSON_PROMPT = """
You are an experienced university lecturer.

Your task is to transform the following lecture notes into a coherent spoken lesson.

Requirements:
- Explain the material naturally.
- Preserve all important information.
- Use smooth transitions between topics.
- If the notes are very concise, add brief explanatory context to improve understanding.
- Keep any additional explanations consistent with the lecture notes.
- Do not invent facts or introduce unrelated information.
- Write as if speaking to a student during a lecture.

Lecture notes:
{lecture_notes}
"""

def generate_lesson(notes):
    prompt = LESSON_PROMPT.format(lecture_notes=notes)
    return ask_llm(prompt)

def render_reading(notes: str):

    with st.spinner("Generating lesson..."):
        lesson = generate_lesson(notes)

    st.markdown(lesson)

    with st.spinner("Generating audio..."):
        audio = synthesize_speech(lesson)

    st.audio(audio, format="audio/wav")