import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)
screen.listen()
score_board=Scoreboard()

player=Player()
car_manager=CarManager()


screen.onkey(player.move,"w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.generate_car()
    car_manager.move_car()

    time.sleep(0.1)
    for car in car_manager.cars:
        if player.distance(car)<24:
            player.reset_player()
            score_board.reset()
            car_manager.cars_reset()

    if player.ycor()>=280:
        score_board.score+=1
        car_manager.move_dist+=10
        player.reset_player()
        score_board.refresh_scoreboard()



screen.exitonclick()