# Updated Streamlit app code with score tracking and comparison to previous score (stored in session state)

updated_app_code = '''
import streamlit as st
import random

# Initialize session state
if "score" not in st.session_state:
    st.session_state.score = 0
if "previous_score" not in st.session_state:
    st.session_state.previous_score = None
if "attempts" not in st.session_state:
    st.session_state.attempts = 0

# Sample question bank
question_bank = {
    "Science": {
        "Plants": [
            {"question": "What is the process by which plants make food?", "options": ["Photosynthesis", "Respiration", "Transpiration"], "answer": "Photosynthesis"},
            {"question": "Which part of the plant conducts photosynthesis?", "options": ["Root", "Stem", "Leaf"], "answer": "Leaf"}
        ],
        "Animals": [
            {"question": "Which animal is a mammal?", "options": ["Shark", "Frog", "Elephant"], "answer": "Elephant"},
        ]
    },
    "History": {
        "India": [
            {"question": "Who was the first Prime Minister of India?", "options": ["Mahatma Gandhi", "Jawaharlal Nehru", "Sardar Patel"], "answer": "Jawaharlal Nehru"}
        ]
    },
    "English": {
        "Grammar": [
            {"question": "What is the noun in the sentence: 'The dog barked loudly'?", "options": ["dog", "barked", "loudly"], "answer": "dog"}
        ]
    }
}

st.title("K-12 Syllabus Reviser")

# Subject and Topic Selection
subject = st.selectbox("Choose a Subject", list(question_bank.keys()))
topic = st.selectbox("Choose a Topic", list(question_bank[subject].keys()))

# Fetch a random question
questions = question_bank[subject][topic]
question_data = random.choice(questions)
question_text = question_data["question"]
options = question_data["options"]
correct_answer = question_data["answer"]

# Display the question
st.subheader("Question:")
st.write(question_text)
user_answer = st.radio("Choose your answer:", options)

# Check the answer
if st.button("Submit Answer"):
    st.session_state.attempts += 1
    if user_answer == correct_answer:
        st.session_state.score += 1
        st.success("Correct! 🎉")
    else:
        st.error(f"Incorrect. The correct answer is: {correct_answer}")

    st.write(f"Your Current Score: {st.session_state.score} out of {st.session_state.attempts}")

    if st.session_state.previous_score is not None:
        st.write(f"Previous Score: {st.session_state.previous_score}")

if st.button("Reset Quiz"):
    st.session_state.previous_score = st.session_state.score
    st.session_state.score = 0
    st.session_state.attempts = 0
    st.success("Quiz has been reset. Previous score saved.")
'''

# Save the updated app code to a new Python file
updated_file_path = "/mnt/data/k12_quiz_app_with_score.py"
with open(updated_file_path, "w") as f:
    f.write(updated_app_code)

updated_file_path
