from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

sc = Screen()
sc.setup(width=800, height=600)
sc.bgcolor("black")
sc.title("Pong Game")
sc.tracer(0)
sc.listen()
r_pad = Paddle(350, 0)
l_pad = Paddle(-350, 0)
ball = Ball()
score = Scoreboard()
# Event handlers
sc.onkey(r_pad.up, "Up")
sc.onkey(r_pad.down, "Down")
sc.onkey(l_pad.up, "w")
sc.onkey(l_pad.down, "s")


game_is_on = True
while game_is_on:
    if (ball.distance(r_pad) < 50 and (340 < ball.xcor() < 345)) or (ball.distance(l_pad) < 50 and
                                                                     (-345 < ball.xcor() < -340)):
        ball.bounce_x *= -1
    elif ball.xcor() > 495:
        score.increase_score(0)
        ball.reset_position()
    elif ball.xcor() < -495:
        score.increase_score(1)
        ball.reset_position()
    ball.move()
    time.sleep(0.0001)
    sc.update()



sc.exitonclick()