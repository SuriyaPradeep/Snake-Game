from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("Black")
screen.tracer(0)  # Restricting from showing the animation
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
# Making snake to move
is_game = True
while is_game:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # distance() is used to find distance between one turtle instance to another or one instance to a point.
    # Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.score_count()
        snake.create_new()

    # Collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        is_game = False

    # Collision with any segments of its  tail
    for segment in snake.segments[1:]:  # List slicing
        if snake.head.distance(segment) < 5:
            scoreboard.game_over()
            is_game = False


screen.exitonclick()
