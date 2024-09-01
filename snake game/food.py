from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.9, stretch_wid=0.9)
        self.color("DarkGreen")
        self.speed(0)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-350, 350)
        random_y = random.randint(-250, 250)
        self.goto(random_x, random_y)
