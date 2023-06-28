import time
from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)

first_player_name = screen.textinput("1st Player", "Name of 1st player:")
first_player_color = screen.textinput("1st Player color", "Your color:")
second_player_name = screen.textinput("2nd Player", "Name of 2nd player:")
second_player_color = screen.textinput("2nd Player color", "Your color:")

r_paddle = Paddle((350, 0), second_player_color)
l_paddle = Paddle((-350, 0), first_player_color)
ball = Ball()

scoreboard = Scoreboard((first_player_name, second_player_name), (first_player_color, second_player_color))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect top/bottom wall hit
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce_y()

    # Detect paddle hit
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
