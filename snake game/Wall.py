from turtle import Turtle


class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.wall_1 = Turtle("square")
        self.wall_1.color("white")
        self.goto(-300, -300)

