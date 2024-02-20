import random

def get_choices(): #function
    player_choice = input("Enter a choice (rock, paper, scissors:)")
    options = ["rock", "paper", "scissors"] #lists
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice} #dictionary
    return choices

def check_win(player, computer ): #arguments within function
    print (f"You chose {player}  , computer chose {computer}")
    if player == computer:
        return ("It's a tie!")
    elif player == "rock":
        if computer == "scissors":
            return "Rock smahes scissors! You Win!"
        else:
            return "Paper cover rock! You Lose."
    elif player == "paper":
        if computer == "scissors":
            return "Paper cover rock! You Win!"
        else:
            return "Scissors cuts paper! You Lose."
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You Win!"
        else:
            return "Rock smashes! You Lose."

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
