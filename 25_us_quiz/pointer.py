from turtle import Turtle


class Pointer(Turtle):
    def __init__(self):
        super(Pointer, self).__init__()
        self.hideturtle()
        self.penup()
        self.color("Black")

    def print(self, data):
        self.goto(data[1], data[2])
        self.write(data[0], align="Center")
