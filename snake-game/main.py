import time
from snake import Snake
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
screen.onkey(snake.key_up, "Up")
screen.onkey(snake.key_left, "Left")
screen.onkey(snake.key_down, "Down")
screen.onkey(snake.key_right, "Right")
screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
