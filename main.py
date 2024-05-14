# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from logo import title
import random

answer = random.randint(1, 100)
MONGON = '''
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
'''
SECRET = f"The correct answer is {answer}"
print(title)
print(MONGON)
print(SECRET)

DIFFICULTY = input("Choose a difficulty. Type 'easy' or 'hard\n")

if DIFFICULTY == "easy":
  chance = 10
  print(f"You have {chance} attempts.\nRemaining to guess the number.")
elif DIFFICULTY == "hard":
  chance = 5
  print(f"You have {chance} attempts.\nRemaining to guess the number.")

# --------------------------------------------------------------------
def Game():
  global chance
  while chance !=0:
    pred = int(input("Make a guess:"))
    if answer == pred:
        return f"You got it! The answer was {answer}."
    elif answer > pred:
      print("Too low.")
      chance -= 1
    elif answer < pred:
      print("Too high.")
      chance -= 1

  if chance == 0:
      return f"Game 0ver. Coreect answer is {answer}!"
# ----------------------------------------------------------

result = Game()
print(result)