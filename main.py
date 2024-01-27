from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=610, height=610)
screen.title("My Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
Scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segment[0].distance(food) < 13:
        food.refresh()
        snake.extend()
        Scoreboard.update()

    elif (snake.segment[0].xcor() > 280 or snake.segment[0].ycor() > 280 or snake.segment[0].xcor() < -280
          or snake.segment[0].ycor() < -280):
        Scoreboard.reset()
        snake.reset()

    for segments in snake.segment[1:]:
        if snake.segment[0].distance(segments) < 10:
            Scoreboard.reset()
            snake.reset()

screen.exitonclick()
