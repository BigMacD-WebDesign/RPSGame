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
game_images = [rock,paper,scissors]

userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
if userChoice >= 3 or userChoice < 0:
    print("You did not enter a valid number! YOU LOSE!")
else:
    print(game_images[userChoice])

    computerChoice = random.randint(0, 2)
    print("Computer Chose:")
    print(game_images[computerChoice])


    if userChoice == 0 and computerChoice == 2:
        print("You win!")
    elif computerChoice == 0 and userChoice == 2:
        print("You Lose!")
    elif computerChoice > userChoice:
        print("You Lose!")
    elif userChoice > computerChoice:
        print("You Win!")
    elif userChoice == computerChoice:
        print("Alright. We'll call it a draw!")