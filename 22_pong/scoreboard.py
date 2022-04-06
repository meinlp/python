from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, 250)
        self.color('white')
        self.l_score = 0
        self.r_score = 0

    def show(self):
        self.clear()
        self.write("Score " + str(self.l_score) + ":" + str(self.r_score),
                   align="Center", font=("Consolas", 20, "normal"))
