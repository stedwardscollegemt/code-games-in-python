# ------ import modules section -----------------------------------------
import turtle as t

# ------ define functions section ---------------------------------------
# todo: define a function draw_star using the sample below
# step 1 - placing the pen at the right location (x, y)
#   t.penup()
#   t.goto(x, y)
#   t.pendown()
# step 2 - calculate the angle using a points variable
#   angle = 180 - (180/points)
# step 3 - start to draw in a colour
#   t.color(colour)
#   t.begin_fill()
# step 4 - for every single point
#   t.forward(size)
#   t.right(angle)
# step 5 - stop drawing
#   t.end_fill()

# ------ algorithm steps section ----------------------------------------
# create the nighttime sky using Turtle graphics
t.Screen().bgcolor('dark blue')

# function call to create a basic yellow star
# 5 points, 50 size, 'yellow' color, x co-ordinate, y co-ordinate
draw_star(5, 50, 'yellow', 0, 0)

# todo create three lists for points, sizes

# todo loop through the list and call the draw_star function to create beautiful stars

input("Please press Enter to end our starry program.")