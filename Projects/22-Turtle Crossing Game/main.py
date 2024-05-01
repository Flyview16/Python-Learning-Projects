import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Set up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Set up player
player = Player()

screen.listen()
screen.onkeypress(player.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
