# ------ import modules section -----------------------------------------

# ------ define functions section ---------------------------------------
def title():
    print("+-+-+-+-+ +-+-+-+-+ +-+-+-+-+")
    print("|R|E|A|L| |F|I|Z|Z| |B|U|Z|Z|")
    print("+-+-+-+-+ +-+-+-+-+ +-+-+-+-+")
    
# ------ algorithm steps section ----------------------------------------
title()

fizzbuzz = []

# loop between numbers 1 and 50 and append to the fizzbuzz list
for number in range(1, 51):
    fizzbuzz.append(number)

# loop through the fizzbuzz list and display elements
for number in fizzbuzz:
    if number % 15 == 0:
        # display "FizzBuzz!"
        print("FizzBuzz!")
    elif number % 5 == 0: 
        # display: "Fizz!"
        print("Fizz!")
    elif number % 3 == 0:
        print("Buzz!")
    else:
        print(number)