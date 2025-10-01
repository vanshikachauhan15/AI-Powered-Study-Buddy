import streamlit as st
from planner import create_study_pack
import json

st.title("AI-Powered Study Buddy (FREE)")
st.write("Runs locally with HuggingFace models – no API key needed!")

text = st.text_area("Paste your notes:", height=300)
num_flashcards = st.slider("Flashcards", 1, 10, 5)
num_mcq = st.slider("MCQ Questions", 1, 5, 3)

if st.button("Generate Study Pack"):
    if not text.strip():
        st.error("Please enter some text.")
    else:
        with st.spinner("Generating..."):
            result = create_study_pack(text, num_flashcards=num_flashcards, num_mcq=num_mcq)

        st.subheader("Summary")
        st.write(result["summary"])

        st.subheader("Explanations")
        for e in result["explanations"]:
            st.write("-", e)

        st.subheader("Flashcards")
        for i, fc in enumerate(result["flashcards"]):
            st.write("Q:", fc["q"])
            st.write("A:", fc["a"])  # Show answer directly

        st.subheader("Quiz")
        for q in result["quiz"]:
            st.write("Q:", q["question"])
            for opt in q["options"]:
                st.write("-", opt)
            st.write("Answer:", q["answer"])

        st.download_button(
            "Download JSON", 
            json.dumps(result, indent=2), 
            "study_pack.json", 
            "application/json"
        )
