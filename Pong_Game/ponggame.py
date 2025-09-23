from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
rpaddle=Paddle(350,0)
lpaddle=Paddle(-350,0)
ball=Ball()
scoreboard=Scoreboard()
screen.listen()
screen.onkeypress(rpaddle.paddle_up,"Up")
screen.onkeypress(rpaddle.paddle_down,"Down")
screen.onkeypress(lpaddle.paddle_up, "w")
screen.onkeypress(lpaddle.paddle_down, "s")


game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
        
    if ball.distance(rpaddle)<50 and ball.xcor()>320 or ball.distance(lpaddle)<50 and ball.xcor()<-320:
        ball.bounce_x()
    
    if ball.xcor()>380:
        ball.refresh()
        scoreboard.lpoint()
    
    if ball.xcor()<-380:
        ball.refresh()
        scoreboard.rpoint()
screen.exitonclick()
