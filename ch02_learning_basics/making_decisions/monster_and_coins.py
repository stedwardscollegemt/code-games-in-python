# ------ import modules section -----------------------------------------

# ------ define functions section ---------------------------------------

# ------ algorithm steps section ----------------------------------------
monsters = 3
coins = 4

print("Do we have more coins than monsters?")
answer = coins > monsters
print(answer)

# display question "Are monsters equal to coins?"
print("Are monsters equal to coins?")
# update the answer variable with the correct boolean expression that compares coins and monster
answer = coins == monsters
# print answer value
print(answer)


# less than
print("Do we have less coins than monsters?")
answer = coins < monsters
print(answer)

# more than one comparison
print("Did you win the game?")
answer = (coins > monsters) or (coins == monsters)
print(answer)