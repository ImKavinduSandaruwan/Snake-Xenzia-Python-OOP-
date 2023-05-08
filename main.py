from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
user_name = screen.textinput(title="Welcome to the game", prompt="Enter your name")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # collision with food
    if snake.snake_head.distance(food) < 15:
        food.refresh_food()
        score.increase_score()
        snake.increase_snake()

    # Collision with wall
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -290 or snake.snake_head.ycor() > 290 or snake.snake_head.ycor() < -290:
        is_game_on = False
        score.game_over(user_name)

    # Collision with tail
    for seg in snake.segments[2:]:
        if seg.distance(snake.snake_head) < 10:
            is_game_on = False
            score.game_over(user_name)

screen.exitonclick()