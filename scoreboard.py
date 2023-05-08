from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("yellow")
        self.goto(0, 260)
        self.hideturtle()
        self.write(f"Score {self.score}", align="center", font=("Arial", 24, "bold"))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score {self.score}", align="center", font=("Arial", 24, "bold"))
        if self.score % 5 == 0:
            self.clear()
            self.write(f"You scored {self.score} points", align="center", font=("Arial", 20, "bold"))

    def game_over(self, name):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=("Arial", 22, "normal"))
        self.goto(0, -20)
        self.write(f"Well Played {name}", align="center", font=("Arial", 15, "normal"))