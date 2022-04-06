from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('Black')
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_is_on = True
sleep = 0.05
while game_is_on:
    time.sleep(sleep)
    screen.update()
    score.show()
    ball.move()
    if score.l_score == 5:
        score.goto(0, 210)
        score.write("Left player wins!!", align="Center", font=("Helvetica", 30, "normal"))
        game_is_on = False

    if score.r_score == 5:
        score.goto(0, 210)
        score.write("Right player wins!!", align="Center", font=("Helvetica", 30, "normal"))
        game_is_on = False

    # detect collision with the wall
    if abs(ball.ycor()) >= 290:
        ball.bounce_y()

    # detect collision with a paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        sleep *= 0.9

    # detect out of bounce
    if ball.xcor() > 380:
        score.l_score += 1
        ball.reset_position()

    if ball.xcor() < -380:
        score.r_score += 1
        ball.reset_position()

    ball.debounce()

    # debug
    print(ball.ycor(), ball.xcor(), ball.y_move, ball.metric, sleep)

screen.exitonclick()
