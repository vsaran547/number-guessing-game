import random
import streamlit as st

st.set_page_config(page_title="Number Guessing Game", page_icon="🎯")

st.title("🎯 Number Guessing Game")
st.write("Choose a difficulty and guess the number.")

DIFFICULTY_RANGES = {
    "Easy (1–10)": 10,
    "Medium (1–100)": 100,
    "Hard (1–1000)": 1000
}

def start_game(max_number):
    st.session_state.max_number = max_number
    st.session_state.secret_number = random.randint(1, max_number)
    st.session_state.attempts = 0
    st.session_state.message = "Game started. Make a guess!"
    st.session_state.game_over = False

if "secret_number" not in st.session_state:
    start_game(100)

difficulty = st.selectbox("Difficulty", DIFFICULTY_RANGES.keys())
max_number = DIFFICULTY_RANGES[difficulty]

if st.button("New Game"):
    start_game(max_number)

guess = st.text_input(f"Guess a number between 1 and {st.session_state.max_number}")

if st.button("Check Guess") and not st.session_state.game_over:
    if not guess.isdigit():
        st.session_state.message = "Please enter a whole number."
    else:
        guess = int(guess)

        if guess < 1 or guess > st.session_state.max_number:
            st.session_state.message = f"Enter a number between 1 and {st.session_state.max_number}."
        else:
            st.session_state.attempts += 1

            if guess < st.session_state.secret_number:
                st.session_state.message = "Too low"
            elif guess > st.session_state.secret_number:
                st.session_state.message = "Too high"
            else:
                st.session_state.message = f"You win! Attempts: {st.session_state.attempts}"
                st.session_state.game_over = True

st.info(st.session_state.message)
st.write(f"Attempts: {st.session_state.attempts}")

