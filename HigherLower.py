from replit import clear
import game_data
from random import choice

Logo = """
     _  _  _        _              
    | || |(_) __ _ | |_   ___  _ _ 
    | __ || |/ _` || ' \ / -_)| '_|
    |_||_||_|\__, ||_||_|\___||_|  
  _          |___/                 
 | |    ___ __ __ __ ___  _ _      
 | |__ / _ \\ V  V // -_)| '_|     
 |____|\___/ \_/\_/ \___||_|       
                                  
"""
vs = """
 **      **  ********
/**     /** **////// 
/**     /**/**       
//**    ** /*********
 //**  **  ////////**
  //****          /**
   //**     ******** 
    //     ////////  
                  
"""
def data():
  return choice(game_data.data)
  
is_not_game_done = True
score =0
while is_not_game_done:
  clear()
  print(Logo)
  if score == 0:
    A = data()
    A_follower = A['follower_count']
  print(f"Compare A: {A['name']}, {A['description']}, {A['country']} ")
  print("\n" + vs )
  B = data()
  print(f"Against B: {B['name']}, {B['description']}, {B['country']} ")
  B_follower = B['follower_count']
  user_choice = input("Who has more followers? Type 'A' or 'B': ")
  if A_follower>B_follower:
    max_follower = 'A'
  else:
    max_follower = 'B'
  if max_follower == user_choice:
    score +=1
    A = B
  else:
    print(f"Oops you choose the wrong one your score {score} ")
    is_not_game_done = False
    
