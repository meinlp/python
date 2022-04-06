from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.shape("turtle")
        self.color("SaddleBrown")
        self.left(90)
        self.shapesize(1.1, 1.1)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)