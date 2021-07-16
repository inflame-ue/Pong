# TODO: 8. Create a scoreboard:

# Import turtle
import turtle


# Create a new scoreboard class
class ScoreBoard(turtle.Turtle):

    def __init__(self, position):
        super().__init__()
        self.ht()
        self.penup()
        self.color("white")
        self.goto(position)
        self.score = 0
        self.write_score()

    def write_score(self):
        self.write(f"{self.score}", False, "center", ("Comic Sans", 40, "normal"))

    def track_score(self):
        self.score += 1
        self.clear()
        self.write_score()
