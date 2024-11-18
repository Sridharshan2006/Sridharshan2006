import streamlit as st
import random

def computer_guessing_game():
    st.header("Computer Guessing Game")
    st.write("Think of a number between 1 and 100.")

    low = 1
    high = 100
    attempts = 0

    with st.form("guessing_form"):
        guess_button = st.form_submit_button(label='Guess')

        if guess_button:
            attempts += 1
            computer_guess = random.randint(low, high)
            st.write(f"Computer's guess: {computer_guess}")

            feedback = st.selectbox("Is the computer's guess:", 
                                    ["Too low", "Too medium (within 10)", 
                                     "Too high", "Correct"])

            if feedback == "Too low":
                low = computer_guess + 1
            elif feedback == "Too high":
                high = computer_guess - 1
            elif feedback == "Too medium (within 10)":
                if computer_guess < high:
                    high = computer_guess + 10
                if computer_guess > low:
                    low = computer_guess - 10
            elif feedback == "Correct":
                st.success(f"Computer guessed the number in {attempts} attempts.")
                st.stop()

def main():
    st.title("Computer Guessing Game App")
    computer_guessing_game()

if __name__ == "__main__":
    main()