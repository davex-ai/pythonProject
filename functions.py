import random


def getchoices():
    print("Welcome To the RPS Game🎉🎉")
    player_choice = input("Rock, Paper, Scissors: ")
    opt = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(opt)
    choices = { "player" : player_choice, "computer": computer_choice }
    return choices

def checkWinner(player, computer):
    if(player == computer):
        return "Its a tie"
def greeting():
    print("Hi")


greeting()
picks = getchoices()
print(picks)