import random


def getchoices():
    print("Welcome To the RPS Game🎉🎉")
    player_choice = input("rock, paper, scissors: ")
    opt = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(opt)
    choices = { "player" : player_choice, "computer": computer_choice }
    check_winner(player_choice, computer_choice)
    return choices

def check_winner(player, computer):
    print("Your choice: " + player + ", Computer Choice: " + computer)
    if player == computer:
        return "Its a tie p🎉"

def greeting():
    print("Hi")


greeting()
picks = getchoices()
print(picks)