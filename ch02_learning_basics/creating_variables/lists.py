# ------ import modules section -----------------------------------------

# ------ define functions section ---------------------------------------
def word_puzzle():
    print("J   L   I   B   P   N   Z   Q   O   A   J   D")
    print("K   B   F   A   M   Z   S   B   E   A   R   O")
    print("O   A   K   T   M   I   C   E   C   T   Q   G")
    print("Y   L   L   S   H   O   E   D   A   O   G   U")
    print("S   L   H   C   O   W   Z   B   T   Y   A   H")
    print("M   H   A   N   D   S   A   O   I   S   L   A")
    print("T   O   P   I   F   Y   P   Y   A   G   J   T")
    print("E   Z   T   B   E   L   T   E   A   T   A   H")

# ------ algorithm steps section ----------------------------------------

# declare a list variable called all_words that contains words the player can find in the puzzle e.g., "BALL", and "BOYE"
all_words = ["SHOE", "HAT", "COW", "BELT", "CAT", "TOYS", "EAR", "BALL", "BATS", "BED", "BOY", "BIG", "MICE"]

print("*** Weclome to Word Play ***")
print("****************************")
print("")

word_puzzle()

# display an instruction to the user e.g. "Can you find all the words?"
print("Can you find all the words?")

# ask the user to enter a word e.g., "Enter a word: "
word = input("Enter a word: ")

# use the list function count() to see if the user input is a good guess, store it in a variable called hit
hit = all_words.count(word)

# display the value of the hit variable
print(hit)


