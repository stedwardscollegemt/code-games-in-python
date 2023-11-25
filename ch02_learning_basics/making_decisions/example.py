# ------ import modules section -----------------------------------------
import random

# ------ define functions section ---------------------------------------
def title():
    print("title")

# ------ algorithm steps section ----------------------------------------
title()

# put all the possible options in a list variable called options_list
options_list = ["rock", "paper", "scissors"]

# use the random module to select a choice from the options_list
player_one = random.choice(options_list)

# ask the user to enter a choice
player_two = input("Enter your choice: rock, paper or scissors")

if player_one == player_two:
    print("You both chose " + player_one + ". No one wins.")

if player_one == "rock" and player_two == "scissors":
    print("Rock breaks scissors. Player one wins!")

# todo: player_one is paper and player_two is scissors
# your code ...

# todo: can you complete more combinations?
# your code ...