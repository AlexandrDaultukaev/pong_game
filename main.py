from turtle import Turtle, Screen
from paddle import Paddle


sc = Screen()
sc.setup(width=800, height=600)
sc.bgcolor("black")
sc.title("Pong Game")
sc.tracer(0)
sc.listen()
pad = Paddle()
# Event handlers
sc.onkey(pad.up, "Up")
sc.onkey(pad.down, "Down")
game_is_on = True
while game_is_on:
    sc.update()



sc.exitonclick()