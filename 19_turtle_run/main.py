from turtle import Turtle, Screen
from random import randint
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')
colors = ['purple', 'blue', 'green', 'yellow', 'orange', 'red']
y = 100
turtles = []
tim_win = False

for i in range(len(colors)):
    tim = Turtle(shape='turtle')
    tim.penup()
    tim.color(colors[i])
    tim.goto(-230, y=y)
    turtles.append(tim)
    y -= 40

while not tim_win:
    for turtle in turtles:
        if turtle.xcor() >= 230:
            tim_win = True
            color = turtle.fillcolor()
            if color == user_bet:
                print("You've won!")
            else:
                print(f"You've lost! The {color} one is winner!")
        turtle.forward(randint(0, 10))

screen.exitonclick()
