from turtle import Turtle


class Snake:

    def __init__(self):
        self.s = []
        self.s = [Turtle(shape="square") for i in range(0, 3)]
        concurrent_x_cord = 0
        for seg in self.s:
            seg.penup()
            seg.color("white")
            seg.setpos(x=concurrent_x_cord - 20, y=0)
            concurrent_x_cord -= 20

    def connect_seg(self):
        for i in range(len(self.s) - 1, 0, -1):
            self.s[i].setpos(x=(self.s[i - 1].xcor()), y=self.s[i - 1].ycor())

    def add_segment(self):
        new_seg = Turtle(shape="square")
        new_seg.penup()
        new_seg.color("white")
        self.s.append(new_seg)

    def go_up(self):
        if self.s[0].heading() != 270:
            self.s[0].seth(90)

    def go_down(self):
        if self.s[0].heading() != 90:
            self.s[0].seth(270)

    def go_left(self):
        if self.s[0].heading() != 0:
            self.s[0].seth(180)

    def go_right(self):
        if self.s[0].heading() != 180:
            self.s[0].seth(0)

    def move_forward(self):
        self.s[0].forward(15)

    def reset(self):
        for seg in self.s[3:]:
            seg.hideturtle()
        self.s = self.s[0:3]
        self.s[0].goto(0, 0)
        self.connect_seg()
