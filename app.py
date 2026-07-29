import streamlit as st

from ui.home import render_homepage

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="🎓",
    layout="wide"
)

render_homepage()