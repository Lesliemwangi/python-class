# functions-> set of code that runs when called
# in python we use def instead of function unlike in javascipt

# dict -> dictonary. Used to enter an array
# key values pair, unique, immutable
# value can be anything
# key and value are seperated by colon
# key and value are seperated by comma
# key and value are enclosed in curly braces
# name is the "key" beau is the "value"

# dict = {"name": "beau", "color": "blue"}

# def greeting():
#     return "Hi"

# # add a variable to return the greeting
# response = greeting()
# print(response)


# lists -> used to store multiple items in a single variable(an array in javascript)
# lists are mutable
# lists are enclosed in square brackets
# lists are seperated by commas
# lists can contain any data type
# lists can be nested, sliced, indexed, iterated over, sorted, reversed, copied, appended, removed, inserted
# lists can be used as a stack or queue, dictionary, set, tuple, map
# lists can be used to store data in a specific order

# food = ["pizza", "carrots", "eggs"]
# print(food)

# dinner = random.choice(food)
# print(dinner)


import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors)")
    # make the computer choices have different options other than one
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)

    choices = {"player": player_choice, "computer": computer_choice}

    return choices
    # return player_choice, computer_choice


# choices = get_choices()
# print(choices)

# refactoring-> the process of restructuring code while keeping the original functionality
# nested if statement -> a statement that will make the code more understandable at a quick glance

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    # we use == instead of = because "=" is the assignment operator that assigns the variables
    # "==" will set an equals sign
    if player == computer:
        return "It's a tie!"
    # elif is "else if" in java script
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
        # else:
        # return "You lose."

# check_win("rock", "paper")
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)

name = "Leslie"
print (name)
# expression -> any type of code that returns a value

 
