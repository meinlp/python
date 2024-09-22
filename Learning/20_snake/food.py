from turtle import Turtle
import random

COLORS_OF_FOOD = ['Sienna', 'DarkOrchid', 'LightSalmon', 'IndianRed', 'LawnGreen', 'LightSeaGreen', 'SteelBlue',
                  'Tomato']


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.speed("fastest")
        self.color(random.choice(COLORS_OF_FOOD))
        self.setpos(random.randint(-13, 13) * 20, random.randint(-13, 13) * 20)

    def refresh(self):
        self.color(random.choice(COLORS_OF_FOOD))
        self.setpos(random.randint(-13, 13) * 20, random.randint(-13, 13) * 20)
