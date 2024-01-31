# ---- import modules --------------------
import random
import time

# ---- define my functions ---------------
def roll_trivial_pursuit_dice():
    colours = ["Pink", "Yellow", "Green", "Blue", "Brown", "Orange"]
    roll = random.choice(colours)
    return roll

# ---- main algorithm steps --------------

# roll the trivia pursuit dice
print("Welcome to Trivial Pursuit, let's roll...")

time.sleep(2)

roll = roll_trivial_pursuit_dice()

if (roll == "Pink"):
    print("Pink: Answer this question in the Art and Literature category.")
elif (roll == "Yellow"):
    print("Yellow: Answer this question in the History category.")
elif (roll == "Green"):
    print("Green: Answer this question in the Science and Nature category.")
elif (roll == "Blue"):
    print("Blue: Answer this question in the Geography category.")
elif (roll == "Brown"):
    print("Brown: Answer this question in the Authors and Literature category.")
else:
    print("Orange: Answer this question in the Sports and Leisure category.")

