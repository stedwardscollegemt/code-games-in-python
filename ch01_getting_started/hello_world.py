import pgzrun

# define functions
def draw():
    screen.draw.text("Hello there, " + name + "!", topleft=(10,10))

# main function
print("*** Welcome to my first program ***")
name = input("Enter your name: ")
pgzrun.go()

