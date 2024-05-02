import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Set up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Set up player and cars
player = Player()
car_manager = CarManager()

screen.listen()
screen.onkeypress(player.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # Detecting collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False



screen.exitonclick()