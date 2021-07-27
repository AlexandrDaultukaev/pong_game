from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.STEP = 4
        self.bounce = 1
        self.shape("circle")
        self.angle_heading = 60
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.setheading(self.angle_heading)

    def bounce_control(self):
        if self.ycor() > 285 or self.ycor() < -285:
            self.bounce *= -1

    def move(self):
        new_x = self.xcor() + self.STEP
        new_y = self.ycor() + self.STEP * self.bounce
        self.goto(new_x, new_y)
        self.bounce_control()
