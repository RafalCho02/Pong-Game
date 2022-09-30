from turtle import Turtle
ALIGMENT = 'center'
FONT = ('PT Mono', 60, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color('white')
        self.penup()
        self.goto(-100, 200)
        self.hideturtle()
        self.write(self.l_score, align=ALIGMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
    def r_point(self):
        self.r_score += 1