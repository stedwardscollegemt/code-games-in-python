"""
@FullName  :
@Date      :
@Title     : Big Quiz Part 2

"""

# ---- import modules ----------------------
import pgzrun

# ---- my global objects -------------------
WIDTH = 1280                            # set width of the screen
HEIGHT = 720                            # set height of the screen

question_box    = Rect(0, 0, 820, 240)
timer_box       = Rect(0, 0, 240, 240)
answer_box1     = Rect(0, 0, 495, 165)
answer_box2     = Rect(0, 0, 495, 165)
answer_box3     = Rect(0, 0, 495, 165)
answer_box4     = Rect(0, 0, 495, 165)

question_box.move_ip(50, 40)
timer_box.move_ip(990, 40)
answer_box1.move_ip(50, 358)
answer_box2.move_ip(735, 358)
answer_box3.move_ip(50, 538)
answer_box4.move_ip(735, 538)

answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

q1 = {
    "q": "What is the capital city of France?",
    "o": ["London", "Paris", "Tokyo", "Berlin"],
    "a": 1
}

q2 = {
    "q": "What is the capital city of France?",
    "o": ["London", "Paris", "Tokyo", "Berlin"],
    "a": 1
}

q3 = {
    "q": "What is the capital city of France?",
    "o": ["London", "Paris", "Tokyo", "Berlin"],
    "a": 1
}

q4 = {
    "q": "What is the capital city of France?",
    "o": ["London", "Paris", "Tokyo", "Berlin"],
    "a": 1
}

q5 = {
    "q": "What is the capital city of France?",
    "o": ["London", "Paris", "Tokyo", "Berlin"],
    "a": 1
}

questions = [q1, q2, q3, q4, q5]

next_question = questions.pop(0)

# set variables to store the player's score and time_left
time_left = 10
score = 0

# ---- define functions --------------------
def draw(): 
    screen.fill("dim gray")
    screen.draw.filled_rect(question_box, "sky blue")
    screen.draw.filled_rect(timer_box, "sky blue")
    for box in answer_boxes:
        screen.draw.filled_rect(box, "orange")

    # draw text for the time_left
    # time_left is a number but it is not supported by draw
    # it needs to be converted to a string
    screen.draw.textbox(str(time_left), timer_box, color=("black"))
    
    # draw text for the next_question["q"] which is the question itself
    screen.draw.textbox(next_question["q"], question_box, color=("black"))

    # loop through each answer box and draw the respective answer option
    index = 0
    options = next_question["o"]
    for box in answer_boxes:
        screen.draw.textbox(options[index], box, color=("black"))
        index += 1

def handle_game_over():
    global next_question
    # set a string variable that stores a message to the user along with the score
    # e.g., "Game over. Your score is 3."
    message = "Game over. Your score is " + str(score)

    # TODO: modify the following dictionary so that "q" maps to the message variable instead
    next_question = {
        "q": message,
        "o": ["-", "-", "-", "-"],
        "a": -1
    }
    
    # update the timer and set it to 0
    time_left = 0

def correct_answer():
    global next_question, score, time_left
    
    # increase the score by 1
    score += 1

    # TODO: if   there are any questions left in the list, 
    #       then pop() the next_question like in line 63 and reset the timer to 10
    #       else handle_game_over()
    # ... your code ...

def on_mouse_down(pos):
    # TODO: create an index variable and set it to 1
    # ... your code ...

    # TODO: loop through each box in answer_boxes
    #            if box.collidepoint(pos) 
    #                  if answer is correct
    #                  then correct_answer()
    #                  else handle_game_over()
    #            increase index by 1
    # ... your code ...
    pass

def update_time_left():
    global time_left
    if (time_left > 0):
        time_left -= 1
    else:
        handle_game_over()

# ---- main algorithm steps ----------------

clock.schedule_interval(update_time_left, 1.0)

# ---- end main ----------------------------

# when we build games using Pygame Zero this should be the very last line
pgzrun.go()