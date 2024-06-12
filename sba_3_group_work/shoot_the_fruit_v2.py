# ---- import modules ----------------------
import pgzrun
import random
import pyodbc

# ---- my global objects -------------------

# screen dimensions
WIDTH = 900
HEIGHT = 500

# fruits
grapes = Actor("grapes")
banana = Actor("banana")
fruits = [grapes, banana]
random_fruit = random.choice(fruits)
screen_text = "Hit the fruit!"

# let us add numerical variables for max_rounds, current_round and points
max_rounds = 10
current_round = 0
points = 0

# let us add a boolean variable for game_over
game_over = False

# some backend stuff we need to track e.g. the id of the player
user_id = -1

# ---- define functions --------------------
def draw():
    screen.clear()
    # let us improve this code so that it "knows" when the game is over
    if game_over:
        screen.draw.text("Game Over!", center=(WIDTH // 2, HEIGHT // 2), fontsize=50, color="red")
        screen.draw.text(screen_text, center=(WIDTH // 2, HEIGHT // 2 + 50), fontsize=30, color="white")
    else:
        random_fruit.draw()
        screen.draw.text(screen_text, topleft=(10,10))

def on_mouse_down(pos):
    # we need to make a lot of improvements here for our game to be playable e.g., check whether game is over, track rounds
    global game_over, screen_text, random_fruit, points, current_round, max_rounds
    if game_over:
        return
    if random_fruit.collidepoint(pos):
        screen_text = "Wow, good aim!"
        points = points + 5
        current_round = current_round + 1
        if current_round >= max_rounds:
            game_over = True
            screen_text = f"Good job you got {points} points" # this is a formatted string
        random_fruit = random.choice(fruits)
        place_fruit(random_fruit)
    else:
        screen_text = "Dang, you missed."

def place_fruit(fruit):
    fruit.x = random.randint(50, WIDTH - 50)
    fruit.y = random.randint(50, HEIGHT - 50)

# ---- backend stuff -----------------------
def connect_db():
    # todo: you probably need the change the absolute path on your computer for it to work
    db_path = r'C:\\Users\\erikacamilleri\\Documents\\GitHub\\code-games-in-python\\sba_3_group_work\\shoot_the_fruit.accdb'
    conn = pyodbc.connect(
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + db_path + ';'
    )
    return conn

def db_users(full_name, username):
    global user_id
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Users WHERE Username = ?', (username,))
    user = cursor.fetchone()
    if user is None:
        cursor.execute('INSERT INTO Users (FullName, Username) VALUES (?, ?)', (full_name, username))
        conn.commit()
        cursor.execute('SELECT @@IDENTITY AS ID')
        user_id = cursor.fetchone()[0]
        print("Welcome to the game new player!")
    else:
        user_id = user[0]
        print("Great to have you back, start shooting!")
    conn.close()



    
# ---- main algorithm steps ----------------
print("Before we start shooting...")
full_name = input("Enter your full name: ")
username = input("Enter your username: ")
db_users(full_name, username)

place_fruit(random_fruit)

# ---- end main ----------------------------
# when we build games using Pygame Zero this should be the very last line
pgzrun.go()