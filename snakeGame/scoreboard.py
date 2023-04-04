from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.sety(250)
        self.hideturtle()
        with open("data.txt") as highscore:
            highscore = highscore.read()
            self.highscore = int(highscore)
        self.write(f"Score: {self.score}    High score: {self.highscore}", False, "center", ("Arial", 20, "bold"))

    def add_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}    High score: {self.highscore}", False, "center", ("Arial", 20, "bold"))

    def game_over(self):
        self.clear()
        self.sety(0)
        self.write(f"New Highscore! : {self.highscore}", False, "center", ("Arial", 16, "bold"))

    def high_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", "w") as highscore:
                highscore.write(str(self.highscore))
            return False
        else:
            return True

    def refresh(self):
        self.clear()
        self.score = 0
        self.write(f"Score: {self.score}    High score: {self.highscore}", False, "center", ("Arial", 20, "bold"))

