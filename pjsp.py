import streamlit as st
import random

def guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    st.header("Guessing Game")
    st.write("Guess a number between 1 and 100.")

    with st.form("guessing_form"):
        user_guess = st.number_input("Enter your guess:", min_value=1, max_value=100)
        submit_button = st.form_submit_button(label='Guess')

        if submit_button:
            attempts += 1
            difference = abs(number_to_guess - user_guess)

            if user_guess == number_to_guess:
                st.success(f"Congratulations! You guessed the number in {attempts} attempts.")
            elif difference < 10:
                st.write("Too medium! You're close, try again.")
            elif user_guess < number_to_guess:
                st.write("Too low! Try again.")
            else:
                st.write("Too high! Try again.")

def main():
    st.title("Guessing Game App")
    guessing_game()

if __name__ == "__main__":
    main()