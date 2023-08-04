from turtle import Turtle

MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:
    def __init__(self):
        self.turtle_list = []
        self.create_snake()
        self.head = self.turtle_list[0]

    def create_snake(self):
        for i in range(3):
            new_t = Turtle("square")
            new_t.penup()
            new_t.color("white")
            new_t.goto(-20 * i, 0)
            self.turtle_list.append(new_t)

    def move(self):
        for i in range(len(self.turtle_list) - 1, 0, -1):
            self.turtle_list[i].goto(self.turtle_list[i - 1].xcor(),
                                     self.turtle_list[i - 1].ycor())
        self.head.forward(MOVE_DISTANCE)

    def key_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def key_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def key_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def key_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


