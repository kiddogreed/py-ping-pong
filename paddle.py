from turtle import Turtle, Screen

STARTING_POS = [(350, 0), (-350, 0)]


class Paddle(Turtle):

    def __init__(self, position):
        """require xy coordinate ex(-350, 0)"""
        super().__init__()
        self.color("red")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(position)

    def up(self):
        current_y = self.ycor()
        current_y += 20
        self.goto(self.xcor(), current_y)

    def down(self):
        current_y = self.ycor()
        current_y -= 20
        self.goto(self.xcor(), current_y)
