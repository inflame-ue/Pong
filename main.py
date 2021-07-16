# TODO: 1. Create the screen.

# Import modules:
import time
import turtle
import scoreboard
import paddle
import ball
import constants as c
import dashline

# The screen:
screen = turtle.Screen()
screen.setup(c.WIDTH, c.HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# TODO: 3. Create a second paddle.

# Create the dash line:
dash_line = dashline.DashLine()

while dash_line.ycor() <= 300:
    dash_line.write_dash_line()

# Create the score:
right_score = scoreboard.ScoreBoard((50, 230))
left_score = scoreboard.ScoreBoard((-50, 230))

# Create the paddle:
right_paddle = paddle.Paddle((370, 0))
left_paddle = paddle.Paddle((-370, 0))

# Create the ball:
ball = ball.Ball()
ball.move_the_ball()

# Control binds:
screen.listen()
screen.onkey(fun=right_paddle.up, key="Up")
screen.onkey(fun=right_paddle.down, key="Down")
screen.onkey(fun=left_paddle.up, key="w")
screen.onkey(fun=left_paddle.down, key="s")

# Screen update:
keep_going = True
while keep_going:
    time.sleep(0.1)
    screen.update()
    ball.move_the_ball()

    # TODO: 5. Detect collisions:
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.revert_y()

    # TODO: 6. Detect collision with paddle:
    if ball.xcor() >= 350 and ball.distance(right_paddle) < 50:
        ball.revert_x()
    elif ball.xcor() <= -350 and ball.distance(left_paddle) < 50:
        ball.revert_x()

    # TODO: 7. Detect when paddle misses the ball:
    # Right paddle
    if ball.xcor() >= 370:
        ball.reset_position()
        right_score.track_score()

    # Left paddle
    if ball.xcor() <= -370:
        ball.reset_position()
        left_score.track_score()

# Exit on click:
screen.exitonclick()
