import pgzrun
import pygame

# draw image
def draw():
    screen.clear()
    turtle_maze_puzzle.draw()

# create a variable and use Actor from pgzero to load an image
# the file must be in an images folder
# always make sure of the spelling and use python conventions
turtle_maze_puzzle = Actor('turtle_maze_puzzle.png')

# the original image is quite large so we scale it down to fit in the screen
turtle_maze_puzzle._surf = pygame.transform.scale(turtle_maze_puzzle._surf, (400, 400))
turtle_maze_puzzle._update_pos()

# use pygamezero to run draw()
pgzrun.go()

quit = input("Press any key to quit...")