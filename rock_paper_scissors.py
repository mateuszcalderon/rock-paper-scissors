# LAST UPDATE: 03/14/2024.
# importing random library we're able to work with pseudo-random types of data.
import random


def get_choice():
    player_choice = input("Enter a choice (rock, paper or scissors): ")
# a list is used to store multiple items in a single variable.
    list_options = ["rock", "paper", "scissors"]
# random.choice will return a random element from the non-empty sequence list_options.
    computer_choice = random.choice(list_options)
# a dictionary is used to store keys and their values.
    dictionary_choices = {"player": player_choice, "computer": computer_choice}
    return dictionary_choices


def check_win(player, computer):
    print(f"You chose {player} and the computer chose {computer}.")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! My bad you lose..."
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissors cuts paper! My bad you lose..."
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You win!"
        else:
            return "Rock smashes scissors! My bad you lose...!"


choices = get_choice()
result = check_win(choices["player"], choices["computer"])
print(result)
