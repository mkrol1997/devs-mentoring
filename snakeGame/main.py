from turtle import Screen
import time
from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(fun=snake.go_up, key="Up")
screen.onkey(fun=snake.go_down, key="Down")
screen.onkey(fun=snake.go_left, key="Left")
screen.onkey(fun=snake.go_right, key="Right")


is_game_on = True

while is_game_on:
    snake.connect_seg()
    snake.move_forward()
    screen.update()
    time.sleep(0.1)
    if snake.s[0].xcor() > 280 or snake.s[0].xcor() < -280 or snake.s[0].ycor() > 230 or snake.s[0].ycor() < -280:
        if score.high_score():
            score.refresh()
            snake.reset()
            screen.update()
        else:
            score.game_over()
            is_game_on = False

    if snake.s[0].distance(food) < 13:
        food.refresh()
        snake.add_segment()
        score.add_score()
    for seg in snake.s[1:]:
        if snake.s[0].distance(seg) < 10:
            if score.high_score():
                snake.reset()
                score.refresh()
                screen.update()
            else:
                score.game_over()
                is_game_on = False

screen.exitonclick()
