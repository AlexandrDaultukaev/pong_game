from turtle import Turtle



class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=0.8)
        self.goto(x=self.x, y=self.y)
        self.color("white")

    def up(self):
        if self.y < 250:
            self.y += 50
        self.goto(x=self.x, y=self.y)

    def down(self):
        if self.y > -250:
            self.y -= 50
        self.goto(x=self.x, y=self.y)
