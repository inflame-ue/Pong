# TODO: 2. Create and move a paddle.

# Import:
import turtle
import constants as c


# Paddle class:
class Paddle(turtle.Turtle):

    def __init__(self, position):
        super().__init__()
        self.speed(0)
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=5)
        self.goto(position)
        self.right(90)

    def move(self):
        self.fd(c.SPEED)

    def up(self):
        self.setheading(c.HEADINGS[0])
        self.move()

    def down(self):
        self.setheading(c.HEADINGS[1])
        self.move()
