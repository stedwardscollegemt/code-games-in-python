# ---- import modules ----------------------
import pgzrun
import random

# ---- my global objects -------------------

# screen dimensions
WIDTH = 900
HEIGHT = 500

# fruits
grapes = Actor("grapes")
banana = Actor("banana")
fruits = [grapes, banana]
random_fruit = random.choice(fruits)
screen_text = "Hit the fruit!"

# let us add numerical variables for max_rounds, current_round and points
max_rounds = 10
current_round = 0
points = 0

# let us add a boolean variable for game_over
game_over = False

# ---- define functions --------------------
def draw():
    screen.clear()
    # let us improve this code so that it "knows" when the game is over
    if game_over:
        screen.draw.text("Game Over!", center=(WIDTH // 2, HEIGHT // 2), fontsize=50, color="red")
        screen.draw.text(screen_text, center=(WIDTH // 2, HEIGHT // 2 + 50), fontsize=30, color="white")
    else:
        random_fruit.draw()
        screen.draw.text(screen_text, topleft=(10,10))

def on_mouse_down(pos):
    # we need to make a lot of improvements here for our game to be playable e.g., check whether game is over, track rounds
    global game_over, screen_text, random_fruit, points, current_round, max_rounds
    if game_over:
        return
    if random_fruit.collidepoint(pos):
        screen_text = "Wow, good aim!"
        points = points + 5
        current_round = current_round + 1
        if current_round >= max_rounds:
            game_over = True
        random_fruit = random.choice(fruits)
        place_fruit(random_fruit)
    else:
        screen_text = "Dang, you missed."

def place_fruit(fruit):
    fruit.x = random.randint(50, WIDTH - 50)
    fruit.y = random.randint(50, HEIGHT - 50)
    
# ---- main algorithm steps ----------------
place_fruit(random_fruit)

# ---- end main ----------------------------
# when we build games using Pygame Zero this should be the very last line
pgzrun.go()