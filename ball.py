from turtle import Turtle
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        current_x = self.xcor() + self.x_move
        current_y = self.ycor() + self.y_move
        self.goto(current_x,current_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()
        self.ball_speed = 0.1




