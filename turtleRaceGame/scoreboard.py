from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.goto(-185, 250)
        self.hideturtle()
        self.write(f"Level: {self.score}", False, "center", FONT)

    def add_score(self):
        self.clear()
        self.score += 1
        self.write(f"Level: {self.score}", False, "center", FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Score: {self.score}", False, "center", FONT)
