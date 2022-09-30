from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import random


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)

ball = Ball()
r_paddle = Paddle((350,0),'red')
l_paddle = Paddle((-350,0),'blue')
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up,'Up')
screen.onkey(r_paddle.go_down,'Down')
screen.onkey(l_paddle.go_up,'w')
screen.onkey(l_paddle.go_down,'s')


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with paddle
    if ball.distance(r_paddle) < 55 and ball.xcor() > 320 or ball.distance(l_paddle) < 55 and ball.xcor() < -320:
        ball.bounce_x()
        random_y =random.randint(0,1)
        if random_y == 1:
            ball.bounce_y()
        ball.speed_up()
    # Detect going r_paddle off screen
    if r_paddle.ycor() > 250:
        r_paddle.goto(350,245)
    if r_paddle.ycor() < -250:
        r_paddle.goto(350,-245)
    # Detect going l_paddle off screen
    if l_paddle.ycor() > 250:
        l_paddle.goto(-350,245)
    if l_paddle.ycor() < -250:
        l_paddle.goto(-350,-245)
    # Detect R paddle misses
    if ball.xcor() > 340 :
        ball.start_position()
        scoreboard.l_point()
        scoreboard.update_scoreboard()
        ball.difficulty_speed()
        r_paddle.goto(350,0)
        l_paddle.goto(-350,0)
    # Detect L paddle misses
    if ball.xcor() < -340:
        ball.start_position()
        scoreboard.r_point()
        scoreboard.update_scoreboard()
        ball.difficulty_speed()
        r_paddle.goto(350, 0)
        l_paddle.goto(-350, 0)

screen.exitonclick()