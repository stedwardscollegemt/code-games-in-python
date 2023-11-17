# Big Questions

Your are encouraged to ask challenging and thought-provoking queries. This will really motivate me to think beyond the basics and explore more complex concepts. This is a fantastic opportunity to tackle more advanced topics. We program to problem-solve and this only happens through collaboration. This section is dedicated to tough questions and to feed your curiosity.

## Matthew asked: "Miss, how do I include an image in my program?"

<u>**Problem**</u>

Matthew wanted to complete the turtle program, but he wanted his program to "know about the context". He wanted his program to display a clear relationship between his result and the maze given. 

<u>**Solution**</u>

To address this problem, he wanted to *upload the image resource* so that the program could display it.

<u>**Python Code**</u>

```python
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
```