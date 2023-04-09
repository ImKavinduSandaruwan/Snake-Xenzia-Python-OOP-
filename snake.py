from turtle import Turtle,Screen

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIS = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_body_parts = []
        self.create_snake()
        self.head = self.snake_body_parts[0]

    def create_snake(self):
        for position in STARTING_POSITION: # 0 1 2
            self.add_segment(position)


    def add_segment(self, position):
        snake_body = Turtle("square")
        snake_body.color("white")
        snake_body.penup()
        snake_body.goto(position)
        self.snake_body_parts.append(snake_body)

    def extend_snake(self):
        self.add_segment(self.snake_body_parts[-1].position())


    def move(self):
        for potition_num in range(len(self.snake_body_parts)-1, 0, -1): # 2 1 0
            new_x = self.snake_body_parts[potition_num - 1].xcor()
            new_y =  self.snake_body_parts[potition_num - 1].ycor()
            self.snake_body_parts[potition_num].goto(new_x, new_y)
        self.head.forward(MOVE_DIS)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

