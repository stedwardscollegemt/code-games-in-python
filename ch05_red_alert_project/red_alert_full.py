# ---- import modules ----------------------
import pgzrun
import random

# ---- my global objects -------------------
FONT_COLOR = (255, 255, 255)            # use white as the color of our text
WIDTH = 800                             # set width of the screen
HEIGHT = 500                            # set height of the screen
CENTER_X = WIDTH / 2                    # horizontal middle
CENTER_Y = HEIGHT / 2                   # vertical middle
# tuple to store the CENTER of the screen
CENTER = (CENTER_X, CENTER_Y)
FINAL_LEVEL = 6
START_SPEED = 10
# list variable called COLORS storing "blue" and "green"
COLORS = ["blue", "green"] 
# boolean variables for game_over and game_complete
game_over = False
game_complete = False
# number variable for current_level and set it to 1
current_level = 1
stars = []                              # list of stars on screen
animations = []                         # list of animations on screen
# dictionary storing messages as key, value pairs
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

# - A star can be red, blue or green, but we can only create *one* red star
# - We need to return a list of colors for our stars e.g., ["red", "blue", "blue", "green", "blue"]
# - We will create a list with "red" and add random colours for the extra stars
def get_colors_to_create(number_of_extra_stars):
    # a list variable colors_to_create containing a string for the color "red"
    colors_to_create = ["red"]
    # a for loop starting from 0 up to number_of_extra_stars
    for i in range(0, number_of_extra_stars):
        # use the random module to choose green or blue from COLORS in a random_color variable
        random_color = random.choice(COLORS)
        colors_to_create.append(random_color)
    return colors_to_create

# - The star elements are Actors which need to be created to be displayed on screen
# - We need to return a list of star Actors
# - We will loop through all colors in colors_to_create
def create_stars(colors_to_create):
    new_stars = []
    # a for loop through every color in colors_to_create
    for color in colors_to_create:
        star = Actor(color + "_star")
        new_stars.append(star)
    return new_stars

def layout_stars(stars_to_layout):
    global WIDTH
    # calculate the number_of_gaps
    number_of_gaps = len(stars_to_layout) + 1
    # calculate the gap_size
    gap_size = WIDTH / number_of_gaps
    # use the random module to shuffle the stars
    random.shuffle(stars_to_layout)
    # update the star position
    for index, star in enumerate(stars_to_layout):
        new_x_pos = (index + 1) * gap_size
        star.x = new_x_pos

def animate_stars(stars_to_animate):
    # a for loop through every star in stars_to_animate
    for star in stars_to_animate:
        duration = START_SPEED - current_level
        star.anchor = ("center", "bottom")
        animation = animate(star, duration=duration, on_finished=handle_game_over, y=HEIGHT)
        animations.append(animation)

# a function handle_game_over() that sets the global game_over variable to True
def handle_game_over():
    global game_over
    game_over = True

# TODO: add comments to explain what this function is doing
def display_message(heading_text, sub_heading_text):
    screen.draw.text(heading_text, fontsize=60, center=CENTER, color=FONT_COLOR)
    screen.draw.text(sub_heading_text, fontsize=30, center=(CENTER_X, CENTER_Y + 30), color=FONT_COLOR)

def on_mouse_down(pos):
    global stars, current_level
    # go through the list of stars and for every star Actor
    for star in stars:
        # use collidepoint() function to check whether the player clicked on one of the stars
        if star.collidepoint(pos):
            if star.image == "red_star": # if they did, check whether the star image is red_star
                on_red_star_click()
            else:
                handle_game_over()

# a function on_red_star_click()
def on_red_star_click():
    global current_level, stars, animations, game_complete
    stop_animations()
    if current_level < FINAL_LEVEL:
        # the player moves up to another level, unless
        current_level += 1
        stars.clear()
        animations.clear()
    else:
        # player reached final level
        game_complete = True

# a function stop_animations()
def stop_animations():
    global animations
    # loop through animations[]
    for animation in animations:
        if animation.running == True:
            animation.stop()

# ---- main algorithm steps ----------------

# ---- end main ----------------------------

# when we build games using Pygame Zero this should be the very last line
pgzrun.go()