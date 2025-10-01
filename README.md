## AI-Powered Study Buddy 

StudyBuddy is a Python Streamlit app that generates summaries, flashcards, and MCQs from any input text.
It runs locally using HuggingFace models and does not require an API key or backend.

 ## Features:

 Paste Any Text – Add your study notes or lesson content.

AI-Powered Summarization – Summarizes your notes for easy understanding.

Flashcards Generator – Creates flashcards for key points.

MCQ Generator – Generates multiple-choice questions with plausible distractors.

No Backend Needed – Runs entirely locally with Streamlit and Python.


## Tech Stack

Python 3.x – Core language

Streamlit – Web interface

Transformers (HuggingFace) – Summarization and AI logic

Planner.py – Script to generate flashcards and MCQs


 ## Project Structure
StudyBuddy/
│── ai_client.py       # HuggingFace AI wrapper
│── app.py             # Streamlit frontend
│── planner.py         # Flashcards & MCQ generation logic
│── config.py          # Configuration for AI provider & model
│── requirements.txt   # Python dependencies
│── README.md


## Installation

Clone the repository:

git clone https://github.com/your-username/StudyBuddy.git
cd StudyBuddy


Install dependencies:

pip install -r requirements.txt


Run the app:

streamlit run app.py

Open your browser at the address shown by Streamlit (usually http://localhost:8501)


## Usage

Paste your study notes into the text box.

Use the sliders to select the number of flashcards and MCQs.

Click Generate Study Pack.


## The app will display:

Summary of your notes

Explanations of key points

Flashcards with questions and answers

MCQs with correct answers and distractors

Download the study pack as JSON for offline use.


## Contribution

Contributions are welcome!

Fork the repository

Create a feature branch

Submit a pull request
