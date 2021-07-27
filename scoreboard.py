from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.left_pad_score = 0
        self.right_pad_score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, -250)
        self.write(
            f"Score: {self.left_pad_score} : {self.right_pad_score}\n         |\n         |\n         |\n         |\n         "
            f"|\n         | "
            f"\n         |\n         |\n         |\n         |\n         |\n         |\n         |\n         |\n         |\n    "
            f"     |",
            align="center",
            font=("Arial", 20,
                  "normal"))

    def increase_score(self, key):
        if key == 0:
            self.left_pad_score += 1
        else:
            self.right_pad_score += 1
        self.clear()
        self.write(
            f"Score: {self.left_pad_score} : {self.right_pad_score}\n         |\n         |\n         |\n         |\n         "
            f"|\n         | "
            f"\n         |\n         |\n         |\n         |\n         |\n         |\n         |\n         |\n         |\n    "
            f"     |",
            align="center",
            font=("Arial", 20,
                  "normal"))
