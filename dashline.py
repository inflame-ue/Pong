# TODO: 9. Create a dash line:

# Import turtle
import turtle


# Create dash line class:
class DashLine(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.width(5)
        self.color("white")
        self.goto(0, -280)
        self.left(90)

    def write_dash_line(self):
        self.pendown()
        self.fd(20)
        self.penup()
        self.fd(10)
