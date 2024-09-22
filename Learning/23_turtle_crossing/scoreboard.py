from turtle import Turtle
from random import randint

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_level = 1
        self.penup()
        self.hideturtle()
        self.color("White")
        self.goto(-290, 270)
        self.write(f"Level: {str(self.current_level)}",
                   align="Left", font=FONT)

    def update(self):
        self.clear()
        self.write(f"Level: {str(self.current_level)}",
                   align="Left", font=FONT)

    def game_over(self):
        self.goto(0, -5)
        self.write("Game Over!",
                   align="Center", font=FONT)


class Markup(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.hideturtle()
        self.penup()
        self.pensize(3)
        for y in range(-220, 280, 50):
            x_init = round(randint(-300, -270))
            for x in range(x_init, 300, 50):
                self.goto(x, y)
                self.pendown()
                self.forward(20)
                self.penup()
