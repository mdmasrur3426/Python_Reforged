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
---'    ____)____
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

rock_paper_scissor = [rock, paper, scissors]

player_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
computer_input = random.randint(0, 2)
if player_input > 2:
    print("Wrong Input")
else:
    print(rock_paper_scissor[player_input])
    print("Computer chose:")
    print(rock_paper_scissor[computer_input])
    if player_input == 0:
        if computer_input == 1:
            print("Paper beats Rock. Computer wins")
        elif computer_input == 2:
            print("Rock beats Scissors. Player wins")
        else:
            print("Draw!")
    elif player_input == 1:
        if computer_input == 0:
            print("Paper beats Rock. Player wins")
        elif computer_input == 2:
            print("Scissor beats paper. Computer wins")
        else:
            print("Draw!")
    elif player_input == 2:
        if computer_input == 0:
            print("Rock beats Scissors. Computer wins")
        elif computer_input == 1:
            print("Scissor beats paper. Player wins")
        else:
            print("Draw!")
    else:
        print("Wrong input")




