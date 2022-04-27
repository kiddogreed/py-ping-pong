from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import netline

STARTING_POS = [(350, 0), (-350, 0)]
MOVE_DISTANCE = 20
SPEED = 0
segment = []

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game ")
screen.tracer(0)

r_paddle = Paddle(STARTING_POS[0])
l_paddle = Paddle(STARTING_POS[1])
ball = Ball()
scoreboard = Scoreboard()
net = netline.Netline()


game_is_on = True
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

while game_is_on:

    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()


    # detect wall colission
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    #detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
       ball.bounce_x()

       print(ball.ball_speed)
    #detect if r paddle mis
    if ball.xcor() > 380:
        ball.reset_position()

        scoreboard.l_point()
    # detect  l paddle miss
    if ball.xcor() < -380:
           ball.reset_position()
           scoreboard.r_point()





screen.exitonclick()
