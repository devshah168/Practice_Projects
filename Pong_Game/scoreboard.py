from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 80, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.lscore=0
        self.rscore=0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.lscore, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.rscore, align=ALIGNMENT, font=FONT)

    def lpoint(self):
        self.lscore+=1
        self.update_scoreboard()

    def rpoint(self):
        self.rscore+=1
        self.update_scoreboard()
