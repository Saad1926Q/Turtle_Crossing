import turtle
import time
FONT = ("Courier", 16, "normal")


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score=0
        with open("highscore.txt",mode="r") as file:
            self.highscore=file.read()
        self.display_score()

    def display_score(self):
        self.goto(0,280)
        self.write(f"score:{self.score} highscore:{self.highscore}",align="center",font=FONT)


    def refresh_scoreboard(self):
        self.clear()
        self.write(f"score:{self.score} highscore:{self.highscore}", align="center", font=FONT)

    def reset(self):
        if self.score>int(self.highscore):
            with open("highscore.txt",mode="w") as file:
                file.write(str(self.score))
            with open("highscore.txt",mode="r") as file:
                self.highscore=file.read()
        self.score=0
        self.refresh_scoreboard()