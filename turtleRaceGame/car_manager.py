from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []

    def create_car(self):
        for i in range(0, 30):
            car = Turtle("square")
            car.car_speed = STARTING_MOVE_DISTANCE
            car.color(random.choice(COLORS))
            car.penup()
            car.shapesize(1, 2)
            car.seth(180)
            car.goto(random.randint(-280, 250), random.randint(-250, 250))
            self.cars.append(car)

    def car_movement(self):
        for car in self.cars:
            car.forward(car.car_speed)
            if car.xcor() <= -330:
                self.reposition_car(car)

    @staticmethod
    def reposition_car(car):
        car.goto(330, random.randint(-250, 250))

    def level_up(self):
        for car in self.cars:
            car.car_speed += MOVE_INCREMENT

    def is_crashed(self, x_cords, y_cords):
        for car in self.cars:
            if car.ycor() in range(int(y_cords) - 15, int(y_cords) + 15):
                if -25 <= int(x_cords) + int(car.xcor()) < 25:
                    return False
            else:
                continue
        return True
