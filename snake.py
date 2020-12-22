from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_array = []
        self.create_snake()
        self.head = self.snake_array[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle()
        segment.penup()
        segment.shape("square")
        segment.color("white")
        segment.goto(position)
        self.snake_array.append(segment)

    def extend(self):
        # add a new segment
        self.add_segment(self.snake_array[-1].position())

    def move(self):
        for seg_num in range(len(self.snake_array) - 1, 0, -1):
            new_x = self.snake_array[seg_num - 1].xcor()
            new_y = self.snake_array[seg_num - 1].ycor()
            self.snake_array[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def reset(self):
        for seg in self.snake_array:
            seg.goto(1000, 1000)
        self.snake_array.clear()
        self.create_snake()
        self.head = self.snake_array[0]
