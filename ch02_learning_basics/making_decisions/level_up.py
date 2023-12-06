# ------ import modules section -----------------------------------------

# ------ define functions section ---------------------------------------

# ------ algorithm steps section ----------------------------------------
print("**********************************")
print("* Who wants to be a millionaire? *")
print("**********************************")

# declare a list of all levels in a list variable called the money_tree
money_tree = ["$100", "$200", "$300", "$500", "$1000"]

# declare a variable called level to store the current level starting at 0
level = 0

# question for $100
print("Here is your first question for " + money_tree[level] + "...")
print("In the UK, the abbreviation NHS stands for National what Service?")
print("[A] Humanity [B] Household [C] Honour [D] Health")
player_guess = input("Enter your guess: ")
correct_answer = "D"

# if player_guess is equal to (==) correct_answer then level up, else, game is over
if player_guess == correct_answer:
    level = level + 1
    print("Great, level up!")
else:
    print("I am sorry, the game is over. No money for you. :(")

if level == 1:
    # give a $200 question
    print("Here is your first question for " + money_tree[level] + "...")
    print("When is Christmas Eve celebrated?")
    print("[A] 25 December [B] 24 December [C] 31 December [D] 1 January")
    player_guess = input("Enter your guess: ")
    correct_answer = "B"