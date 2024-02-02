# ---- import modules --------------------
import time
import random

# ---- define my functions ---------------
def choose_random_scene():
    scenes = ["Beach", "Kitchen", "Space", "Jungle", "City"]
    scene = random.choice(scenes)
    return scene

# def a function that accepts a scene and returns a list of items
def get_scene_items(scene):
    beach_items = ["sun", "umbrella"]
    kitchen_items = ["fridge", "pot"]
    space_items = ["meteor", "alien"]
    jungle_items = ["tiger", "tree"]
    city_items = ["car", "school"]
    if scene == "Beach":
        return beach_items
    elif scene == "Kitchen":
        return kitchen_items
    elif scene == "Space":
        return space_items
    elif scene == "Jungle":
        return jungle_items
    elif scene == "City":
        return city_items

# ---- main algorithm steps --------------
print("Welcome to the 'I Spy' game!")
print("You have 60 seconds to identify items in the scene. Ready? Let's go!")

time_limit = 15
start_time = time.time()
is_time_up = ((time.time() - start_time) > time_limit)

score = 0

# starting a round
scene = choose_random_scene()
items = get_scene_items(scene)

print("I Spy with my little eye... items at a ", scene)

# while there is time left, accept user guesses and display the state of the game
while (is_time_up == False):
    guess = input("Your guess: ").lower()
    guess_correct = guess in items
    if guess_correct == True:
        score = score + 1
        print("Wow, good guess! Keep trying.")
    else:
        print("Nope, sorry. Try again.")
    is_time_up = ((time.time() - start_time) > time_limit)

print("Time is up! Your score: ", score)