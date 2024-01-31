# ---- import modules --------------------
import time
# todo: random

# ---- define my functions ---------------
def choose_random_scene():
    scenes = ["Beach", "Kitchen", "Space", "Jungle", "City"]
    # todo: return a random scene

# todo: def a function that accepts a scene and returns a list of items

# ---- main algorithm steps --------------
print("Welcome to the 'I Spy' game!")
print("You have 60 seconds to identify items in the scene. Ready? Let's go!")

start_time = time.time()
is_time_up = (time.time() - start_time < time_limit)

# todo: while there is time left, accept user guesses and display the state of the game

print("Time is up! Your score: ", score)