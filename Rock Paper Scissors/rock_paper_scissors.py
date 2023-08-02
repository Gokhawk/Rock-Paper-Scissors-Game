import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

possibilities = [rock, paper, scissors] # Adding possibilities to a list for making a choice 
while True:   # Used while loop to restart the game if user wants to replay 
   user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n:")
   if user_choice == "0":
       print(rock)
       computer_choice = random.choice(possibilities) # Random module helps us to randomize the choice of computer. 
       if computer_choice == paper: # I used multiple if statements to predict the computer's choice 
           print("Computer chosed:")
           print(paper)
           print("You Lose.")
           retry = input("Try Again ? y/n : ").lower()
           if retry == "n":
              print("Leaving game...")
              break
       if computer_choice == scissors:
           print("Computer chosed:")
           print(scissors)
           print("You Win!")
           retry = input("Try Again ? y/n : ").lower()
           if retry == "n":
              print("Leaving game...")
              break
       if computer_choice == rock:
           print("Computer chosed:")
           print(rock)
           print("Draw.")
           retry = input("Try Again ? y/n : ").lower()
           if retry == "n":
              print("Leaving game...")
              break

   if user_choice == "1":
       print(paper)
       computer_choice = random.choice(possibilities)
       if computer_choice == paper:
          print("Computer chosed:")
          print(paper)
          print("Draw.")
          retry = input("Try Again ? y/n : ").lower()
          if retry == "n":
              print("Leaving game...")
              break
       if computer_choice == scissors:
          print("Computer chosed:")
          print(scissors)
          print("You Lose")
          retry = input("Try Again ? y/n : ").lower()
          if retry == "n":
              print("Leaving game...")
              break
       if computer_choice == rock:
          print("Computer chosed:")
          print(rock)
          print("You Win!")
          retry = input("Try Again ? y/n : ").lower()
          if retry == "n":
              print("Leaving game...")
              break

   if user_choice == "2":
       print(scissors)
       computer_choice = random.choice(possibilities)
       if computer_choice == paper:
          print("Computer chosed:")
          print(paper)
          print("You Win!")
          retry = input("Try Again ? y/n : ").lower()
          if retry == "n":
              print("Leaving game...")
              break
       if computer_choice == scissors:
          print("Computer chosed:")
          print(scissors)
          print("Draw.")
          retry = input("Try Again ? y/n : ").lower()
          if retry == "n":
              print("Leaving game...")
              break
       if computer_choice == rock:
          print("Computer chosed:")
          print(rock)
          print("You Lose.")
          retry = input("Try Again ? y/n : ").lower()
          if retry == "n":
              print("Leaving game...")
              break
   else:
        retry = input("You selected invalid number. Do you want to try again ? y/n : ").lower()  # I used this else statement because if user selects and invalid number, user can restart or quit the game.
        if retry == "n":
            print("Leaving game...")
            break
