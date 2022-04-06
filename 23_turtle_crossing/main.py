import time
from turtle import Screen
from player import Player, STARTING_POSITION
from car_manager import CarManager
from scoreboard import Scoreboard, Markup
from random import randint, choice

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("SlateGray")
screen.tracer(0)

# initializing
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
markup = Markup()
for i in range(4):
    car_manager.create_car(randint(-250, 250))


# keyboard tracking
screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
spawn_timer = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    print(spawn_timer)
    if spawn_timer <= 0:
        car_manager.create_car(300)
        spawn_timer += round(randint(0, int(25 * (0.9 ** int(scoreboard.current_level)))))
        # debug - spawn speed
        # print(spawn_timer)
    else:
        spawn_timer -= 1

    for car in car_manager.all_cars:
        if car.xcor() < -300:
            car_manager.destroy_car(car)
            # debug - cars on the screen
            # print(len(car_manager.all_cars))
        if player.distance(car) < 21: # and (player.ycor() - car.ycor()) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() >= 290:
        scoreboard.current_level += 1
        scoreboard.update()
        player.goto(STARTING_POSITION)
    car_manager.move(scoreboard.current_level)

screen.exitonclick()
