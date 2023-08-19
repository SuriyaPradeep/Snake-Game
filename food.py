from turtle import Turtle
import random


class Food(Turtle):  # Here turtle is superclass
    def __init__(self):
        super().__init__()
        # Calls init of the superclass
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_len=.5, stretch_wid=.5)  # Changes the size
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
