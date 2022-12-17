from random import randint
def mode(level):
  if level == "easy":
    return 10
  elif level == "hard":
    return 5
  else:
    return "Wrong choice"

def game_play(attempt,computer_guess):
  print(f"You have {attempt} remaining to guess the number")
  user_guess = int(input("Make a guess: "))
  if user_guess > computer_guess:
    print("Too high")
    return 0
  elif user_guess < computer_guess:
    print("Too low")
    return 0
  else:
    print("You guess it correct")
    return 1

def modify_attempt():
  return attempt -1
  
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
difficulty=input("Choose a difficulty.Type 'easy' or 'hard': ")
computer_guess = randint(1,100)
attempt = mode(difficulty)

while attempt >0:
  win_loose =game_play(attempt,computer_guess)
  attempt = modify_attempt()
  if win_loose == 1:
    break
