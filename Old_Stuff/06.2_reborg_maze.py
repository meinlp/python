def turn_round():
    turn_left()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def go_right():
    turn_right()
    move()


count = 0

while not at_goal():
    if count == 3:
        turn_round()
        move()
        turn_left()
        move()
        count = 0
    elif right_is_clear():
        go_right()
        count += 1
    elif front_is_clear():
        move()
        count = 0
    else:
        turn_left()
        count = 0