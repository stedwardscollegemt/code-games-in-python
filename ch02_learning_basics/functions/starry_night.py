# ------ import modules section -----------------------------------------
import turtle as t

# ------ define functions section ---------------------------------------

# define a function draw_star using the sample below
def draw_star(points, size, colour, x, y):
    # step 1 - placing the pen at the right location (x, y)
    t.penup()
    t.goto(x, y)
    t.pendown()
    # step 2 - calculate the angle using a points variable
    angle = 180 - (180/points)
    # step 3 - start to draw in a colour
    t.color(colour)
    t.begin_fill()
    # step 4 - for every single point
    for p in range(0, points):
        t.forward(size)
        t.right(angle)
    # step 5 - stop drawing
    t.end_fill()

# ------ algorithm steps section ----------------------------------------
# create the nighttime sky using Turtle graphics
t.Screen().bgcolor('dark blue')

# function call to create a basic yellow star
# 5 points, 50 size, 'yellow' color, x co-ordinate, y co-ordinate
draw_star(5, 50, 'yellow', 0, 0)

# create four lists for points, sizes, colours, coordinates
star_points = [5, 7, 9, 11]
star_sizes = [50, 20, 60, 10] 
star_colours = ['yellow', 'orange', 'red', 'green']
star_xy = [0, -20, 50, 30]

# loop through the list and call the draw_star function to create beautiful stars
index = 0
for star_p in star_points:
    draw_star(star_points[index], star_sizes[index], star_colours[index], star_xy[index], star_xy[index])
    index = index + 1


input("Please press Enter to end our starry program.")