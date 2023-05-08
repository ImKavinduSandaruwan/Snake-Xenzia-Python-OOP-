from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("cyan")
        self.shapesize(stretch_wid=0.7, stretch_len=0.7)
        self.refresh_food()

    def refresh_food(self):
        self.penup()
        self.goto(x=random.randint(-280, 280), y=random.randint(-280, 280))