import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

score = Scoreboard()
player = Player()
cars = CarManager()
cars.create_car()
cars = cars
screen.listen()

game_is_on = True


while game_is_on:
    cars.car_movement()
    screen.onkey(player.go_forward, "Up")
    player_x = player.xcor()
    player_y = player.ycor()
    if not cars.is_crashed(player_x, player_y):
        player.hideturtle()
        screen.update()
        score.game_over()
        game_is_on = False
        break
    else:
        if player.ycor() >= FINISH_LINE_Y:
            score.add_score()
            cars.level_up()
            player.reset()
    time.sleep(0.1)
    screen.update()


screen.exitonclick()
