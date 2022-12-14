from replit import clear
import requests
import json
hangmanpic = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

hangman=""" 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                    """

print(hangman+"\n")

words = requests.get('https://random-word-api.herokuapp.com/word')
word = json.loads(words.text)[0].lower()

display =['_']*len(word)

lives =0 


end_of_game = False
while not end_of_game:
  user_choice = input("Enter the letter: ").lower()
  clear()
  print(hangman+"\n")
  if user_choice in display:
    print(f"You already guess {user_choice} letter\n")
  else:
    for pos in range(len(word)):
      if word[pos] == user_choice:
        display[pos] = user_choice
    if user_choice not in word:
      print(f"You guess {user_choice} letter not in word,You loose a life.\n")
      print(hangmanpic[lives])
      lives +=1
    print(f"{' '.join(display)}")
    if '_' not in display:
      end_of_game=True
      print("You Win")
    if lives == 7:
      print(f"You loose , The word is {word}")
      end_of_game=True
      
    
