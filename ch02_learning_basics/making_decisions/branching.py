# ------ import modules section -----------------------------------------
import random

# ------ define functions section ---------------------------------------
def title():
    print("+-+-+-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+")
    print("|R|E|V|E|R|S|E| |F|I|Z|Z| |B|U|Z|Z|")
    print("+-+-+-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+")
    
# ------ algorithm steps section ----------------------------------------

print("Let us play...")

title()

# ask the user whether they know how to play this game
response = input("Do you know how to play this game? (yes/no) ")

# ---- one branch example -----------------------------------------------
# if the user does not know how to play, display instructions or do a practice round
if response == 'no':
    print("Imagine a list of instructions...")
    print("Let's practice: 1, 2, Fizz!")
    print("Notice that instead of 3, I said Fizz!")

# get a random number between 1 and 50 from the user
number_in = input("Enter a number between 1 and 50: ")

# get a random number using the random module just in case
number = random.randint(1, 50)

# ---- two branches example ----------------------------------------------
# if not number_in.is_numeric(), display error message, game will continue with random number
# else, number = int(number_in)
if not number_in.is_numeric():
    print("Error, game will continue with a random number")
else:
    number = int(number_in)
    
# ---- more than two branches example ------------------------------------
if number % 15 == 0:
    # display "FizzBuzz!"
    print("FizzBuzz!")
elif number % 5 == 0: 
    # display: "Fizz!"
    print("Fizz!")
# todo else if number mod 3 == 0, then display "Buzz!"
else:
    print(number)

print("This game will be more fun and challenging once we learn about loops!")