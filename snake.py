from turtle import Turtle


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_FORWARD = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segment = []
        self.create()
        self.head = self.segment[0]

    def create(self):
        for i in STARTING_POSITIONS:
            self.add_segment(i)

    def add_segment(self, position):
        tom = Turtle(shape="circle")
        tom.color("white")
        tom.penup()
        tom.goto(position)
        self.segment.append(tom)

    def reset(self):
        for i in self.segment:
            i.goto(10000, 100000)
        self.segment.clear()
        self.create()
        self.head = self.segment[0]

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        for seg in range(len(self.segment)-1, 0, -1):
            new_x = self.segment[seg-1].xcor()
            new_y = self.segment[seg-1].ycor()
            self.segment[seg].goto(new_x, new_y)
        self.head.forward(MOVE_FORWARD)

    def up(self):
        if self.segment[0].heading() != DOWN:
            self.segment[0].setheading(UP)

    def down(self):
        if self.segment[0].heading() != UP:
            self.segment[0].setheading(DOWN)

    def left(self):
        if self.segment[0].heading() != RIGHT:
            self.segment[0].setheading(LEFT)

    def right(self):
        if self.segment[0].heading() != LEFT:
            self.segment[0].setheading(RIGHT)
