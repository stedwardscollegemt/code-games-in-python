# ------ import modules section -----------------------------------------

# ------ define functions section ---------------------------------------
def title():
    print("")
    print("█▀▄▀█ █▀▀█ ▀▀█ █▀▀ 　 █▀▀ █▀▀█ █▀▀█ ▀▀█ █▀▀")
    print("█░▀░█ █▄▄█ ▄▀░ █▀▀ 　 █░░ █▄▄▀ █▄▄█ ▄▀░ █▀▀")
    print("▀░░░▀ ▀░░▀ ▀▀▀ ▀▀▀ 　 ▀▀▀ ▀░▀▀ ▀░░▀ ▀▀▀ ▀▀▀")
    print("")

# ------ algorithm steps section ----------------------------------------

title()

# todo: create string variables to store a 10 by 20 maze by creating 10 strings that are 20 characters long
# Walls: █ ▀
# Food: .
# Path: ' '
# Destination: *
# Player: P
maze_row_1 = "█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█"
maze_row_2 = "█ .      ▀▀  . . P █"
# your code... get creative :)

# todo: write print statements under each other to display to entire maze
# your code

# display the width of our maze
maze_row_length = len(maze_row_1)
print("Maze Width: ", maze_row_length)

# todo: display the number of food items '.' in the entire maze
food_count = maze_row_1.count(".") + maze_row_2.count(".")
# your code...