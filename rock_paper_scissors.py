#this code lets you play a simple game of rock, scissors, paper
#it was made just for the python practice 

import random
from enum import IntEnum

class Action(IntEnum):
    rock = 0
    paper = 1
    scissors = 2

def get_user_selection():
    user_action = input("Choose your action (rock[0], paper[1], or scissors[2]): ")
    selection = int(user_action)
    action = Action(selection)
    return action

def get_computer_selection():
    selection = random.randint(0, len(Action) - 1)
    action = Action(selection)
    return action

def choose_winner(user_action, computer_action):
    if user_action == computer_action:
        print(f"Both players have played the same action. Tie!")
    elif user_action == Action.rock:
        if computer_action == Action.scissors:
            print("Your rock smashes the computers scissors. You win!")
        else:
            print("The computer's paper covers your rock. You lose!")
    elif user_action == Action.paper:
        if computer_action == Action.rock:
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == Action.scissors:
        if computer_action == Action.paper:
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

while True:
    try:
        user_action = get_user_selection()
    except:
        print("Invalid action. Try entering [0], [1], or [2]: ")
        continue
    computer_action = get_computer_selection()
    choose_winner(user_action, computer_action)

    prompt = input( "Play again? y/n: ")
    if prompt != 'y':
        break

