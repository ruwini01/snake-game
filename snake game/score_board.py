from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.count = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.pencolor("White")
        self.penup()
        self.goto(0, 270)
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(arg=f"Score: {self.count} High Score: {self.high_score}", move=False, align="center", font=FONT)

    def increase_score(self):
        self.count += 1
        self.clear()
        self.update_score_board()

    def reset(self):
        if self.count > self.high_score:
            self.high_score = self.count
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.count = 0
        self.update_score_board()

    # def game_over(self)
    # self.goto(0, 0)
    # self.write("GAME OVER", False, ALIGNMENT, FONT)
