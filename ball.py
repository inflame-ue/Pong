# TODO: 4. Create the ball and make it move:

# Import modules:
import turtle


# Create ball class:
class Ball(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x = 10
        self.y = 10

    def move_the_ball(self):
        x = self.xcor() + self.x
        y = self.ycor() + self.y
        self.goto(x, y)

    def revert_y(self):
        self.y *= -1

    def revert_x(self):
        self.x *= -1

    def reset_position(self):
        self.home()
        self.revert_x()
