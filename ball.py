from turtle import Turtle
import random
y_move_options = [10, -10]
x_move_options = [10, -10]
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.x_move = random.choice(y_move_options)
        self.y_move = random.choice(x_move_options)
        self.move_speed = 0.06
        # self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)
    def bounce_y(self):
        self.y_move *= -1
    def speed_up(self):
        self.move_speed *= 0.8
    def difficulty_speed(self):
        self.move_speed = 0.06
    def bounce_x(self):
        self.x_move *= -1
    def start_position(self):
        self.goto(0,0)