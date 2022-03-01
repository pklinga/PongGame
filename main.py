from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
screen = Screen()
scoreboard = Scoreboard()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

is_game_on = True
while is_game_on:
    while is_game_on and ball.ycor() < 290:
        time.sleep(ball.delay)
        screen.update()
        ball.move()

        #Detect collision with the wall.
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_wall()
            ball.move()

        #Detect collision with the paddle and increase speed.
        if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
            ball.bounce_paddle()

        #Detect goal on right
        if ball.xcor() > 400:
            ball.reset_ball()
            scoreboard.l_point()

        #Detect goal on left
        if ball.xcor() < -400:
            ball.reset_ball()
            scoreboard.r_point()

screen.exitonclick()