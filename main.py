import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.screensize(canvwidth=800, canvheight=600)
screen.title("Pong")

screen.tracer(0)

pad1 = Paddle(350)
pad2 = Paddle(-350)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(pad1.go_up, "Up")
screen.onkey(pad1.go_down, "Down")
screen.onkey(pad2.go_up, "w")
screen.onkey(pad2.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(pad1) < 50 and ball.xcor() > 340 or ball.distance(pad2) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_points()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_points()

screen.exitonclick()
