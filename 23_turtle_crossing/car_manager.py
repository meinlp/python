from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.spawn_location = [-245, -195, -145, -95, -45, 5, 55, 105, 155, 205, 255]
        self.ban = []

    def create_car(self, x):
        # this is for avoiding spawn on the same lane
        if len(self.ban) == 4:
            for i in self.ban:
                self.spawn_location.append(i)
            self.ban = []

        # car parameters
        new_car = Turtle("square")
        new_car.penup()
        new_car.color(choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.move_distance = STARTING_MOVE_DISTANCE

        # this is for avoiding spawn on the same lane
        new_y = int(choice(self.spawn_location))
        self.spawn_location.remove(new_y)
        self.ban.append(new_y)
        new_car.goto(x, new_y + round(randint(-5, 5)))

        # add car to car list
        self.all_cars.append(new_car)
        # debug
        # print(self.ban, self.spawn_location)

    def destroy_car(self, car):
        car.hideturtle()
        self.all_cars.remove(car)

    def move(self, quantifier):
        for car in self.all_cars:
            car.goto(car.xcor() - (STARTING_MOVE_DISTANCE + MOVE_INCREMENT * (quantifier - 1)), car.ycor())
