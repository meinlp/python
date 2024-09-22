import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.pensize(1)
tim.hideturtle()
tim.speed(10)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_random():
    for _ in range(100):
        tim.pencolor(random_color())
        choice = random.choice(["left", "right", "NaN"])
        if choice == "left":
            tim.left(90)
        elif choice == "right":
            tim.right(90)
        tim.forward(20)


def draw_a_square(size):
    for _ in range(4):
        tim.forward(size)
        tim.right(90)


def draw_dashed_line(length, dash, space):
    iterations = round(length / (dash + space))
    # print(iterations)
    for _ in range(iterations):
        tim.forward(dash)
        tim.penup()
        tim.forward(space)
        tim.pendown()
    remain = length - iterations * (dash + space)
    if remain > 0:
        if remain <= dash:
            tim.forward(remain)
        else:
            tim.forward(dash)
            tim.penup()
            tim.forward(remain - dash)


def draw_shape(a, b):
    angle = 360 / a
    tim.right(angle / 2)
    for _ in range(int(360 / angle)):
        tim.forward(b)
        tim.right(angle)
    tim.left(angle / 2)


def draw_spirograph(r, a):
    for _ in range(round(360 / a)):
        tim.pencolor(random_color())
        tim.circle(r)
        tim.right(a)


screen = t.Screen()
screen.exitonclick()
