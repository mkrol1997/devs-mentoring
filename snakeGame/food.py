from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        x_cord = randint(-280, 280)
        y_cord = randint(-280, 220)
        self.goto(x_cord, y_cord)

    def refresh(self):
        x_cord = randint(-280, 280)
        y_cord = randint(-280, 220)
        self.goto(x_cord, y_cord)
