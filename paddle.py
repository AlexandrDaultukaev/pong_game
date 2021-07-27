from turtle import Turtle



class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.x = 350
        self.y = 0
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=4, stretch_len=0.8)
        self.goto(x=self.x, y=self.y)
        self.color("white")

    def up(self):
        if self.y < 250:
            self.y += 70
        self.goto(x=self.x, y=self.y)


    def down(self):
        if self.y > -250:
            self.y -= 70
        self.goto(x=self.x, y=self.y)
