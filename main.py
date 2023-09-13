from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
screen = Screen()
screen.title("Adeola's Pong Game")
screen.bgcolor("Black")
screen.setup(800, 600)
screen.tracer(0)

r_paddle=Paddle((370,0))
l_paddle=Paddle((-370,0))
ball=Ball()
scoreboard=Scoreboard()



screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
game_is_on=True
# Add a variable to track if a collision has occurred
collision_occurred = False

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collisions with wall
    if ball.ycor() < -275 or ball.ycor() > 275:
        ball.bounce_y()

    # Detect collisions with paddles
    if (
        (ball.distance(r_paddle) < 50 and ball.xcor() > 340)
        or (ball.distance(l_paddle) < 50 and ball.xcor() < -340)
    ):
        if not collision_occurred:  # Check if a collision has already occurred
            ball.bounce_x()
            collision_occurred = True  # Set the flag to True after bouncing
    else:
        collision_occurred = False  # Reset the flag if there's no collision

    # Detect when right paddle misses
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_point()

    # Detect when left paddle misses
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
