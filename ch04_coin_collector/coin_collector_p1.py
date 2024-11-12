"""
@FullName  :
@Date      :
@Title     : Coin Collector Part 1

"""
import pgzrun

def draw():
 screen.fill("green")
 fox.draw()
 coin.draw()
 screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))

WIDTH = 400
HEIGHT = 400
score = 0
game_over = False

fox = Actor("fox")
fox.pos = 100, 100
coin = Actor("coin")
coin.pos = 200, 200



pgzrun.go()