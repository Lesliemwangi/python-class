import random

# Function to get the choices of the player and the computer
def get_choices():
    # Get the player's choice
    player_choice = input("Enter a choice (rock, paper, scissors):")
    # make the computer choices have different options other than one
    # Define the computer's choice options
    options = ["rock", "paper", "scissors"]
    # Get the computer's choice
    # Randomly select the computer's choice
    computer_choice = random.choice(options)
    
    # Store the choices in a dictionary
    choices = {"player": player_choice, "computer": computer_choice}

    return choices

# Function to check the winner
def check_win(player, computer):
    # Print the choices of the player and the computer
    print(f"You chose {player}, computer chose {computer}")
    # Check if the choices are the same
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose."
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissors cuts paper! You lose."
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You win!"
        else:
            return "Rock smashes scissors! You lose."
        
# Get the choices
choices = get_choices()

# Check the winner
result = check_win(choices["player"], choices["computer"])

# Print the result
print(result)