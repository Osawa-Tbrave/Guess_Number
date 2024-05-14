import streamlit as st
from logo import title
import random

st.markdown(title, unsafe_allow_html=True)

answer = random.randint(1, 100)
MONGON = '''
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
'''
st.write(MONGON)

DIFFICULTY = st.selectbox("Choose a difficulty. Type 'easy' or 'hard'", ('easy', 'hard'))

if DIFFICULTY == "easy":
  chance = 10
  st.write(f"You have {chance} attempts.\nRemaining to guess the number.")
elif DIFFICULTY == "hard":
  chance = 5
  st.write(f"You have {chance} attempts.\nRemaining to guess the number.")

def Game():
  global chance
  while chance !=0:
    pred = st.number_input("Make a guess:", min_value=1, max_value=100, step=1)
    if answer == pred:
        return f"You got it! The answer was {answer}."
    elif answer > pred:
      st.write("Too low.")
      chance -= 1
    elif answer < pred:
      st.write("Too high.")
      chance -= 1

  if chance == 0:
      return f"Game 0ver. Correct answer is {answer}!"

if st.button('Guess!'):
    result = Game()
    st.write(result)
