# ------ import modules section -----------------------------------------

# ------ define functions section ---------------------------------------
def cherry():
    print("\n")
    print("   __.--~~.,-.__    ")
    print("  `~-._.-(`-.__`-.  ")
    print("          \    `~~` ")
    print("    .--./ \         ")
    print("   /#   \  \.--.    ")
    print("   \    /  /#   \   ")
    print("    '--'   \    /   ")
    print("            '--'    ")
    print("\n")

# ------ algorithm steps section ----------------------------------------

# create variable to store the number (integer) of points
points = 670

# todo: create a variable to store the number (integer) of bonus points and set it to 0
# ... your code ...

# todo: update the bonus variable to contain 25% of the points entered
# ... your code ...

# todo: update points value to reflect to correct amount of total points earned
# ... your code ...

# todo: display the number of points e.g. "Points: 250" using the print()
# ... your code ...

# if the user got over 500 points they win a special cherry in the game
if points > 500:
    cherry()
else:
    print("You did not collect enough points to win a cherry token.")

