# ---- import modules --------------------

# ---- define my functions ---------------
def title():
    print("A nice title to get bonus marks!")

def pick_a_random_word():
    # todo: code that picks a random word
    return "secret"

def update_clue(secret, guesses):
    # todo: secret with question marks for letters not guessed
    return ['?', '?', '?']


# ---- main algorithm steps --------------
    
# select a random word from the list
    
# keep track of lives and guessed letters

# loop condition to end the game when all lives are lost
lives_remaining = True

while lives_remaining:
    # get updated clue

    # check if clue reveals secret, this is a win
    if clue == secret:
        print("You guessed the secret word! You win!")
        break
    
    # not a win yet, enable user to guess a letter

    # provide feedback to the user after each guess
        
    # keep track of lives and guessed letters

