# ------ import modules section -----------------------------------------
import random

# ------ define functions section ---------------------------------------

# ------ algorithm steps section ----------------------------------------
print("************************")
print("*** Guess The Number ***")
print("************************")

# get a random number using the random module
number = random.randint(1, 10)

# todo: display a message "We have thought of a number, can you guess?"
# your code...

# accept a guess input from the user
guess_in = input("Enter your guess between 1 and 10")

# convert user guess into an integer so that we can make comparisons
guess = int(guess_in)

# todo: create a boolean variable is_guessed that checks whether guess is equal to number
# your code...

# todo: ask for the user to keep guessing while not is_guessed... else, the user won!
# your code...

# todo: why not include a break and give the user three chances to guess?