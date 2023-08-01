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

possibilities = [rock, paper, scissors]
while True:
   user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n:")
   if user_choice == "0":
       print(rock)
       computer_choice = random.choice(possibilities)
       if computer_choice == paper:
           print("Computer chosed:")
           print(paper)
           print("You Lose.")
           retry = input("Try Again ? y/n : ")
           if retry == "n":
              print("Leaving game...")
              break
       if computer_choice == scissors:
           print("Computer chosed:")
           print(scissors)
           print("You Win!")
           retry = input("Try Again ? y/n : ")
           if retry == "n":
              print("Leaving game...")
              break
       if computer_choice == rock:
           print("Computer chosed:")
           print(rock)
           print("Draw.")
           retry = input("Try Again ? y/n : ")
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
          retry = input("Try Again ? y/n : ")
          if retry == "n":
              print("Leaving game...")
              break
       if computer_choice == scissors:
          print("Computer chosed:")
          print(scissors)
          print("You Lose")
          retry = input("Try Again ? y/n : ")
          if retry == "n":
              print("Leaving game...")
              break
       if computer_choice == rock:
          print("Computer chosed:")
          print(rock)
          print("You Win!")
          retry = input("Try Again ? y/n : ")
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
          retry = input("Try Again ? y/n : ")
          if retry == "n":
              print("Leaving game...")
              break
       if computer_choice == scissors:
          print("Computer chosed:")
          print(scissors)
          print("Draw.")
          retry = input("Try Again ? y/n : ")
          if retry == "n":
              print("Leaving game...")
              break
       if computer_choice == rock:
          print("Computer chosed:")
          print(rock)
          print("You Lose.")
          retry = input("Try Again ? y/n : ")
          if retry == "n":
              print("Leaving game...")
              break
   else:
        retry = input("You selected invalid number. Do you want to try again ? y/n : ")
        if retry == "n":
            print("Leaving game...")
            break