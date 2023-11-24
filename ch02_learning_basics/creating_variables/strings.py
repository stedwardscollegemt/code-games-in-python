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
maze_row_3 = "█ . █              █"
maze_row_4 = "█ .            █ . █"
maze_row_5 = "█ . ▀▀▀▀▀▀▀▀▀▀▀▀ . █"
maze_row_6 = "█ .      ▀▀  . . . █"
maze_row_7 = "█ . . . . . . . .  █"
maze_row_8 = "█ . ▀▀▀▀▀▀▀▀▀▀▀▀ * █"
maze_row_9 = "█ . █              █"
maze_row_10 = "▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀"

# write print statements under each other to display to entire maze
print(maze_row_1)
print(maze_row_2)
print(maze_row_3)
print(maze_row_4)
print(maze_row_5)
print(maze_row_6)
print(maze_row_7)
print(maze_row_8)
print(maze_row_9)
print(maze_row_10)

# display the width of our maze
maze_row_length = len(maze_row_1)
print("Maze Width: ", maze_row_length)

# display the number of food items '.' in the entire maze
food_count = maze_row_1.count(".") + maze_row_2.count(".") + maze_row_3.count(".") + maze_row_4.count(".") + maze_row_5.count(".") + maze_row_6.count(".") + maze_row_7.count(".") + maze_row_8.count(".") + maze_row_9.count(".") + maze_row_10.count(".")
print("Food Count: ", food_count)
