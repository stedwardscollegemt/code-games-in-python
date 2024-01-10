# ------ import modules section -----------------------------------------
import random

# ------ define functions section ---------------------------------------

# ------ algorithm steps section ----------------------------------------
print("************************")
print("*** Guess The Number ***")
print("************************")

# get a random number using the random module
number = random.randint(1, 10)

# display a message "We have thought of a number, can you guess?"
print("We have thought of a number, can you guess?")

# accept a guess input from the user
guess_in = input("Enter your guess between 1 and 10:  ")

# convert user guess into an integer so that we can make comparisons
guess = int(guess_in)

# create a boolean variable is_guessed that checks whether guess is equal to number
is_guessed = (guess == number)

# ask for the user to keep guessing while not is_guessed... otherwise, the user won!
chances = 3
while(not is_guessed):
    guess_in = input("Enter another guess between 1 and 10:  ")
    guess = int(guess_in)
    is_guessed = (guess == number)
    chances = chances - 1
    if chances == 0:
        print("Sorry you did not guess in four chances! The number was", number)
        break

if is_guessed:
    print("Wow! You won.")