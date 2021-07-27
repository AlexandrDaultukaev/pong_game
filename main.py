from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

sc = Screen()
sc.setup(width=800, height=600)
sc.bgcolor("black")
sc.title("Pong Game")
sc.tracer(0)
sc.listen()
l_pad = Paddle(350, 0)
r_pad = Paddle(-350, 0)
ball = Ball()
# Event handlers
sc.onkey(l_pad.up, "Up")
sc.onkey(l_pad.down, "Down")
sc.onkey(r_pad.up, "w")
sc.onkey(r_pad.down, "s")
game_is_on = True
while game_is_on:
    ball.move()
    time.sleep(0.0001)
    sc.update()



sc.exitonclick()