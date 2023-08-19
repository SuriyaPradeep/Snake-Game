from turtle import Turtle

START_POS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for i in START_POS:
            self.add_segments(i)

    def add_segments(self, position):
        tur = Turtle(shape="square")
        tur.color("white")
        tur.penup()
        tur.goto(position)
        self.segments.append(tur)

    def create_new(self):
        self.add_segments(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):  # To move from highest to lowest
            x_coordinate = self.segments[i - 1].xcor()
            y_coordinate = self.segments[i - 1].ycor()
            self.segments[i].goto(x_coordinate, y_coordinate)
        self.head.forward(10)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
