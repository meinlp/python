from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.metric = 0

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        if self.metric == 0:
            self.y_move *= -1
            self.metric += 5

    def bounce_x(self):
        if self.metric == 0:
            self.x_move *= -1
            self.metric += 5

    def debounce(self):
        if self.metric > 0:
            self.metric -= 1

    def reset_position(self):
        # self.bounce_y()
        self.bounce_x()
        self.goto(0, 0)
