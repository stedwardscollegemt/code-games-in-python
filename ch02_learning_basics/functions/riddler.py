# ------ import modules section -----------------------------------------
import time

# ------ define functions section ---------------------------------------
def title():
    print("+-+-+-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+")
    print("        |R|I|D|D|L|E|R|            ")
    print("+-+-+-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+")
    
# ------ algorithm steps section ----------------------------------------
title()

riddle = "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?"
clue = "You would probably hear it in a large cave."
answer = "echo"

# Let us code a typing effect to display the riddle using functions
#       - print(char, end="", flush=True)
#       - time.sleep(delay)
for char in riddle:
    print(char, end="", flush=True)
    time.sleep(0.3)

# Give the user two chances to guess, for the second chance display the clue
chances = 2
is_guessed = False
while(chances > 0 and is_guessed == False):
    print(f"You have {chances} chances to guess. Please type a guess:")
    guess = input()
    is_guessed = guess == answer
    if is_guessed:
        print("Wow, you are so smart! You beat the riddler.")
        break
    else:
        chances = chances - 1
        if chances == 1:
            for char in clue:
                print(char, end="", flush=True)
                time.sleep(0.1)

if (not is_guessed):
    print("The riddler has beat you! The answer was: ", answer)
