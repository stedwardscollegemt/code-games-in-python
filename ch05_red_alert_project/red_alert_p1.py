# ---- import modules ----------------------
import pgzrun
# TODO: import random module

# ---- my global objects -------------------
FONT_COLOR = (255, 255, 255)            # use white as the color of our text
WIDTH = 800                             # set width of the screen
HEIGHT = 500                            # set height of the screen
CENTER_X = WIDTH / 2                    # horizontal middle
CENTER_Y = HEIGHT / 2                   # vertical middle
# TODO: [new] tuple to store the CENTER of the screen
# ... your code ...
FINAL_LEVEL = 6
START_SPEED = 10
# TODO: list variable called COLORS storing "blue" and "green"
# ... your code ...
# TODO: boolean variables for game_over and game_complete
# ... your code ...
# TODO: number variable for current_level and set it to 1
# ... your code ...
stars = []                              # list of stars on screen
animations = []                         # list of animations on screen
# TODO: [new] dictionary storing messages as key, value pairs
messages = {
    "lose": "Try again.",
    "win": "Great job."
}

# ---- define functions --------------------
def draw(): 
    global stars, current_level, game_over, game_complete 
    screen.clear()
    screen.blit("space_bg", (0, 0)) 
    if game_over: 
        display_message("GAME OVER!", messages["lose"]) 
    elif game_complete: 
        display_message("YOU WON!", messages["win"])
    else:
        for star in stars:
            star.draw()

def update():
    global stars
    if len(stars) == 0:
        stars = make_stars(current_level)

def make_stars(number_of_extra_stars):
    colors_to_create = get_colors_to_create(number_of_extra_stars)
    new_stars = create_stars(colors_to_create)
    layout_stars(new_stars)
    animate_stars(new_stars)
    return new_stars

def get_colors_to_create(number_of_extra_stars):
    return []

def create_stars(colors_to_create):
    return []

def layout_stars(stars_to_layout):
    pass 

def animate_stars(stars_to_animate):
    pass

# ---- main algorithm steps ----------------

# ---- end main ----------------------------

# when we build games using Pygame Zero this should be the very last line
pgzrun.go()