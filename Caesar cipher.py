logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)

def caesar(message,shift,direction):
  text = ""
  if direction == "decode":
    shift *= -1
  for letter in message:
    if letter in alphabet:
      pos = alphabet.index(letter)
      new_position = pos + shift
      text += alphabet[new_position]
    else:
      text +=letter
  print(f"The {direction} text is {text}")

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


should_continue = "True"
while should_continue:
  direction =  input("Type 'encode' to encrypt , 'decode' to decrypt\n")
  text = input("Enter you message\n").lower()
  shift = int(input("Type the shift number\n"))
  shift = shift%26
  caesar(text,shift,direction)
  choice = input("Type 'yes' if you want to continue, 'no' for exit\n").lower()
  if choice == 'no':
    should_continue = False
print("Good Bye")
  
  
    
    

