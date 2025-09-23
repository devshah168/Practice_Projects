from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(x,y)
        


        
    def paddle_up(self):
        y=self.ycor()
        self.sety(y+20)
        
    def paddle_down(self):
        y=self.ycor()
        self.sety(y-20)
    