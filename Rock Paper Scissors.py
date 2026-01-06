import random

def getchoices():
    print("Welcome To the RPS Game🎉🎉")
    player_choice = input("rock, paper, scissors: ")
    opt = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(opt)
    choices = { "player" : player_choice, "computer": computer_choice }
    return choices

def check_winner(player, computer):
    print(f"Your choice: {player}, Computer Choice: {computer}")
    if player == computer:
        return "Its a tie 🎉"
    elif player == "rock" and computer == "scissors":
        return "Player Wins"
    elif player == "rock" and computer == "paper":
        return "Computer Wins"
    elif player == "paper" and computer == "rock":
        return "Player Wins"
    elif player == "paper" and computer == "scissors":
        return "Computer Wins"
    elif player == "scissors" and computer == "paper":
        return "Player Wins"
    elif player == "scissors" and computer == "rock":
        return "Computer Wins"
    else:
        print("Invalid option")

picks = getchoices()
res = check_winner(picks["player"], picks["computer"])
print(res)