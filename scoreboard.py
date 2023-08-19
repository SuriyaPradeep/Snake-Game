from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 15, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as f:
            self.high_score = int(f.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setposition(0, 275)
        self.update_score()

    def game_over(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as f:
                self.high_score=self.score
                f.write(str(self.high_score))
        self.goto(0,0)
        self.color("red")
        self.write("GAME OVER", align="center", font=("Arial", 25, "bold"))

    def update_score(self):
        self.clear()
        # write is used to write anything in the turtle screen
        self.write(f"Score:{self.score}  High Score:{self.high_score}", align=ALIGNMENT, move=False, font=FONT)

    def score_count(self):
        self.score += 1
        self.update_score()
