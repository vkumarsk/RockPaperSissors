import random
from enum import IntEnum

class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3
    Spock = 4

victories = {
    Action.Scissors: [Action.Lizard, Action.Paper],
    Action.Paper: [Action.Spock, Action.Rock],
    Action.Rock: [Action.Lizard, Action.Scissors],
    Action.Lizard: [Action.Spock, Action.Paper],
    Action.Spock: [Action.Scissors, Action.Rock]
}

def player():
    choice = [f"{action.name}[{action.value}]" for action in Action]
    selection_string = ", ".join(choice)
    player_selection = int(input(f"Enter a choice ({selection_string}): "))
    action = Action(player_selection)
    return action

def computer():
    computer_selection = random.randint(0, len(Action) - 1)
    action = Action(computer_selection)
    return action

def game(user_action, computer_action):
    defeats = victories[user_action]
    if user_action == computer_action:
       computer()
    elif computer_action in defeats:
        print(f"{user_action.name} beats {computer_action.name}! You win!")
    else:
        print(f"{computer_action.name} beats {user_action.name}! You lose.")

while True:

    user_action = player()
    computer_action = computer()
    game(user_action, computer_action)

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break