from turtle import Turtle

class Netline(Turtle):

    def __init__(self):
        super().__init__()
        self.color("green")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=0.2, stretch_wid=50)
        self.goto(0,0)