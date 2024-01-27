from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.color("white")

    def refresh(self):
        rand_x = randint(-285, 285)
        rand_y = randint(-285, 285)
        self.goto(rand_x, rand_y)
