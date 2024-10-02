# Chapter 2 Learning Basics

We make use of <b>variables</b> in our programs to store and label data elements like a piece of text or a number. We will make use of these constructs regularly - for instance, to hold the user score in a game, or keep track on how many lives are left. We might need to store different data elements in different scenarios.

## Creating Variables

### How to create a variable

To create a variable we must give it a unique name and it is a good idea to pick a name that briefly describes what data is being stored. What the variable then stores is called a <b>value</b>. When we create a variable and give it a value we normally say *_assigning a value to a variable_*.

For example:

```
score = 0
print(score) # we can output the value of score to the screen
```
<pre>
0
</pre>

### Using numbers

As we already say, we can use variables to store a whole number or `integer` which in turn can be used in arithmetic calculations.

An example of a simple calculation:

```
x = 2
y = x * 3
print(y) 
```

<pre>
6
</pre>

At any point in the program you can change the value of a variable. All you need to do is assign it to a different value.

```
x = 5
print(y) # Do you think the value of y will change now?
```
<pre>
6
</pre>

You guessed it. For `y` to reflect the new value of `x` we need to perform the calculation again. This is because the computer executes statements line by line and to get the results expected our instructions need to be written in the correct order.

```
x = 5
y = x * 3
print(y)
```
<pre>
15
</pre>

Simple mathematical operators:

|  Symbol  | Meaning | Usage       |
| -------- | ------- |-------------|
| +        | plus    | `z = x + y` |
| -        | minus   | `z = x - y` |
| *        | times   | `z = x * y` |
| /        | divide  | `z = x / y` |

More difficult mathematical operators:

|  Symbol  | Meaning      | Usage       |
| -------- | ------------ |-------------|
| //       | floor divide | `z = x // y`|
| %        | remainder    | `z = x % y` |
| **       | power        | `z = x ** y`|

When we code, different types of numbers can be stored in our variables. Whole numbers are of type `integer` and numbers with a decimal point in them are of type `float`. Both types of numbers can be used in arithmetic calculations.

### Working with strings

A <b>string</b> is data that is made up of <b>a sequence of letters or other characters</b> like punctuation symbols and numbers. Words and sentences are stored as strings in our programs. Most programs use at least one of these kind of variables. Anything that you can type in your keyboard can be stored in a string variable. When using the `input()` function to ask the user to type something you should treat the value as a string.

```
favourite_colour = "orange"
print(favourite_colour)
```

Python gives us a lot of <b>built-in functionality</b> to work with our string variables.

1. We can join strings together using the `+` operator

```
favourite_colour = input("Enter your favourite colour: ") # ask user to enter a value
sentence = "Your favourite colour is " + favourite_colour + "."
print(sentence)
```
<pre>
Enter your favourite colour: 
orange
Your favourite colour is orange.
</pre>

2. We can get the length of a string using the `len()` function

```
message = "Hey there, giraffe..."
message_length = len(message) # we need to store the length in a variable to use it later
print(message_length)
```
<pre>
21
</pre>

3. Other string functions you can experiment with on a string variable e.g. `str`

|  Function  | Description                          | Usage                       | Example            |
| ---------- | ------------------------------------ | --------------------------- | ------------------ |
| `strip()`  | Remove leading and trailing spaces   | `str.strip()`               | `"  hi  " >> "hi"` |
| `lower()`  | Convert characters to lower case     | `str.lower()`               | `"Hi" >> "hi"`     |
| `upper()`  | Convert characters to upper case     | `str.upper()`               | `"Hi" >> "HI"`     |
| `count()`  | Count occurrance of a letter or word | `str.count(phrase)`         | `"Hi", "i" >> 1`   |

```
message = "   Hey there, giraffe...   "
message = message.strip() # our string variable is message in this case
print(message)
```
<pre>
"Hey there, giraffe..."
</pre>

### Making lists

Simple variables are great but we also need to be able to store a group of data items. We can create <b>list</b> variables to <b>store multiple data items under one label</b>. There are many use cases in which lists could be useful in games. For example, a list can store a deck of cards for a game of Twenty-One. Upon request, the next card is dealt from the list. A deck consists of 52 unique cards, so rather than creating 52 variables to store cards, we can store all the card values in a list variable.

```
deck = ["1 hearts", "2 hearts", "3 hearts", "4 hearts", "5 hearts", "6 hearts"]
```

Every value in a list has a <b>unique position</b> which is identified with a number. The very first position in the list has a value of 0. We can use the position to get individual values from a list variable.

To access a memory location within a list we need to type the name of the list variable e.g., `deck`, followed by the item's position in the list within square brackets `[]`, e.g., `[2]`. To access the third data item we write `deck[2]`. Here is an example:

```
firstItem = deck[0] # a single value in a list can be treated like a simple variable
thirdItem = deck[2]

print(firstItem)
print(thirdItem)
print(deck[0])
print(deck[2])
```

<pre>
1 hearts
3 hearts
1 hearts
3 hearts
</pre>

Python gives us a lot of <b>built-in functionality</b> to work with our list variables. Some functions will already seem familiar to you.

1. We can get the length of a list using the `len()` function

```
numbers = [10, 5, 8, 9]
numbers_length = len(numbers) # we need to store the length in a variable to use it later
print(numbers_length)
```
<pre>
4
</pre>

2. We can get the number of occurrances of a data item in a list using the `count()` function

```
fruit = ["apple", "orange", "apple", "kiwi", "banana"]
count_apple = fruit.count("apple")
print(count_apple)
```
<pre>
2
</pre>

3. Other list functions you can experiment with on a list variable e.g. `mylist`

|  Function  | Description                          | Usage                       |
| ---------- | ------------------------------------ | --------------------------- |
| `append()` | Add a data item at the end of list   | `mylist.append(item)`       |
| `clear()`  | Remove all data items in a list      | `mylist.clear()`            |
| `insert()` | Put a data item at a position        | `mylist.insert(pos, item)`  |
| `pop()`    | Get the last item and remove it      | `mylist.pop()`              |
| `remove()` | Remove one data item from the list   | `mylist.remove(item)`       |
| `reverse()`| Reverse the position list items      | `mylist.reverse() `         |
| `sort()`   | Sort data items in ascending order   | `mylist.sort()`             |

## Making decisions

Decision making is an important part of our logical thinking and it is often based on answers to questions like, "Do I have any lives yet?" or, "Am I close to reaching the high score?". We want our algorithms to have this ability to "make decisions". Making computers answer human questions is obviously difficult, but, computers are very good at <b>comparing two values</b> and most of the time this is enough to create very interesting game play.

### Making comparisons

The questions that computers are able to answer have only two possible outcomes: `True` or `False`. You know by now that these two <b>Boolean</b> values are the backbone of computer science because they represent <b>binary</b>. You can create variables that store a Boolean value, just note that in Python, these values are special words and must start with a capital letter.

```
answer_true = True
answer_false = False
```

The questions our algorithms will ask are essentially made up of a series of <b>comparisons between two values</b>. A computer is able to <b>make comparisons</b> by using <b>logical operators</b>. These questions are actually called <b>Boolean expressions</b>.

```
player_age = 7
are_they_equal = (player_age == 10) # Boolean expression
print(are_they_equal) 
```

<pre>
False
</pre>

|  Symbol  | Meaning     | Boolean Expression       | Question                         |
| -------- | ----------- |--------------------------|----------------------------------|
| ==       | equal to    | `x == y`                 | Is x <b>equal to</b> y?          |
| !=       | not equal to| `x != y`                 | Is x <b>not equal to</b> y?      |
| <        | less than   | `x < y`                  | Is x <b>less than</b> y?         |
| >        | greater than| `x > y`                  | Is x <b>greater than</b> y?      |

Do you remember how we illustrate decision making in flowcharts?

![flowchart if-else statement](https://raw.githubusercontent.com/stedwardscollegemt/code-games-in-python/bc0737e41804e73f7217b92d97134204aa0355a9/img/ch02_md_diamond.drawio.svg)

Simple questions in the Python language use the following format:

```
if answer_true: 
    print("Yes, answer is True!")
else:
    print(No, answer is False!)
```

Example:

```
x = 12
y = 5
if x < y:
   print("x is less than y")
else:
   print("x is greater or equal to y")
```
<pre>
x is greater or equal to y
</pre>

### Multiple comparisons using logic gates

To make multiple comparisons or ask more complex questions in one statement we use <b>logic gate operations</b> like `and`, `or` and `not`. 

```
monters = 3
coins = 4

is_game_over = (monters == 4 or coins == 0) # complex Boolean expression that evaluates to True or False

if is_game_over == True
   print("Game over!")
```
Remember from <a target="blank" href="">Chapter 10</a> that when using `or` only one answer needs to be `True` for the entire expression to be `True`, when using `and`, all answers need to be `True` for the expression to be `True`.

For example, let us imagine that to go up a level in a game the player must have collected at least 1 star <b>and</b> score over 500 points. First, we will create variables to store the amount of stars and the points. Then, we write a Boolean expression so that the algorithm can decide whether another level is unlocked or not.

```
score = 493
stars = 2

if score > 500 and stars > 0:
   print("Congratulations, you unlocked a new level!")
else:
   print("Oh no. Seems like you are stuck. Better luck next time.")
```
<pre>
Oh no. Seems like you are stuck. Better luck next time.
</pre>

### Branching 

You probably already guessed that we pose questions in a certain way so that the <b>computer can decide which parts of our program need to run</b> based on a <b>condition</b> or <b>test</b>. When we write have multiple code blocks but only one should run, we call it <b>branching</b>.

1. One branch

This is the simplest example which is an `if` statement on its own. There is only one outcome, so only one branch. The code snippet in the branch will run only when the condition is `True`.

```
spells = 11
if spells > 10:
   print("You gained the title Enchanter!")
```

In this example, we are simply checking whether the value of <b>spells is greater than 10</b>, this is our Boolean expression. If the expression is `True`, for instance, if spells has a value of 12, then the player will receive a message "You gained the title Enchanter!". However, nothing special happens when the condition is `False` and the program will skip the message display and proceed with the rest of the program.

2. Two branches

This is the example we have used before where if an expression is `True` then one code snippet will run, if `False` then an alternative snippet will run. Since there are two possible outcomes then we have two branches for which we can use an `if-else` statement.

Recall the example of deciding whether a player has unlocked a level:

```
if score > 500 and stars > 0:
   print("Congratulations, you unlocked a new level!")
else:
   print("Oh no. Seems like you are stuck. Better luck next time.")
```

For a player to go up a level he must have collected at least 1 star and gained over 500 points. The expression is made up of <b>two conditions</b> with an `and` in between. Both conditions need to be `True` for the player to see the good news on screen. In the event that the Boolean expression is `False` then the player needs to try again, so the program jumps to execute the `else` statement. 

3. More than two branches

When we have three or more possible outcomes, we need to use the `elif` command.

```
lives = 1
pellets = 36

if lives == 0:
   print("Game over!")
elif pellets == 50:
   print("Woo-hoo! Press Enter key to go to the next level.")
else:
   print("Watch out for those ghosts!")
```
In this program, we are imagining a game of Pac-Man. The player is initially given three lives and has to navigate a complex maze containing pellets that need to be eaten. Except, there are ghosts in the maze and if the player gets eaten by a ghost, a live is lost.

There is a hard rule that when all lives are lost the game ends. This is the first branch. Therefore, when the value of lives is equal to zero, the player sees "Game over!". But, in the chance that the player managed to eat all the pellets (and lives still remain) then the player is automatically passed to the next level. This is the second branch. If neither of these hard rules are `True` then the player is still trying to win the level, and so for encouragement the game prints out "Watch out for those ghosts!". This is the third branch.

You always must use an `elif` after an `if` and before an `else`.

## Playing With Loops 

Computers are good at doing repetitive tasks without getting bored, unlike ourselves. Looping structures like `while` and `for` loops can be used to run the same block of code over and over again. 

## Functions 


