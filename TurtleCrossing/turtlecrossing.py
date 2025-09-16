from turtle import Turtle,Screen
import time
from player import Player
from scoreboard import Scoreboard
from carmanager import CarManager


screen=Screen()
screen.setup(width=600,height=600)
screen.listen()
screen.tracer(0)
player=Player()
carmanager=CarManager()
scoreboard=Scoreboard()
screen.onkey(player.goup,"w")


game_is_on=True
while game_is_on:

    time.sleep(0.1)
    screen.update()
    
    carmanager.create_car()
    carmanager.move()
    
    for car in carmanager.all_cars:
        if car.distance(player)<20:
            game_is_on=False
            scoreboard.game_over()
    
    if player.is_finish():
        player.go_start()
        carmanager.inc_speed()
        scoreboard.inc_score()
screen.exitonclick()
