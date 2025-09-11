from turtle import Turtle,Screen

tim=Turtle()
screen = Screen()
screen.listen()
def forward():
    tim.forward(10)

def backwards():
    tim.backward(10)

def counterclockwise():
    new_heading=tim.heading()+10
    tim.setheading(new_heading)

def clockwise():
    new_heading=tim.heading()-10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.onkey(fun=forward,key="w")
screen.onkey(fun=backwards, key="s")
screen.onkey(fun=counterclockwise, key="a")
screen.onkey(fun=clockwise, key="d")
screen.onkey(fun=clear, key="c")


screen.exitonclick()
