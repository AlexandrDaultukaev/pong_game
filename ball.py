from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.STEP = 4
        self.penup()
        self.bounce_x = 1
        self.bounce_y = 1
        self.shape("circle")
        self.angle_heading = 60
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.setheading(self.angle_heading)

    def bounce_control(self):
        if self.ycor() > 285 or self.ycor() < -285:
            self.bounce_y *= -1

    def move(self):
        new_x = self.xcor() + self.STEP * self.bounce_x
        new_y = self.ycor() + self.STEP * self.bounce_y
        self.goto(new_x, new_y)
        self.bounce_control()

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x *= -1
