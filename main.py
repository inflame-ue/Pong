# TODO: 1. Create the screen.

# Import modules:
import turtle
import random
import paddle


# The screen:
screen = turtle.Screen()
screen.screensize(canvwidth=800, canvheight=600, bg="black")
screen.title("Pong")
screen.tracer(0)

# TODO: 3. Create a second paddle.

# Create the paddle:
first_paddle = paddle.Paddle((390, 0))
second_paddle = paddle.Paddle((-390, 0))

# Control binds:
screen.listen()
screen.onkey(fun=first_paddle.up, key="Up")
screen.onkey(fun=first_paddle.down, key="Down")
screen.onkey(fun=second_paddle.up, key="w")
screen.onkey(fun=second_paddle.down, key="s")

# Check the boarders:
if first_paddle.ycor() >= 300:
    first_paddle.down()
elif first_paddle.ycor() <= -300:
    first_paddle.up()

# Screen update:
keep_going = True
while keep_going:
    screen.update()










# Exit on click:
screen.exitonclick()
