from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score_Board
import time

# Setup screen
screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("The Pong Game")

# Game Objects
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
score = Score_Board()

# Game Control Flags
game_is_on = True
is_paused = False

# Functions
def toggle_pause():
    global is_paused
    is_paused = not is_paused

def restart_game():
    global is_paused
    ball.reset_ball()
    score.reset_scoreboard()
    l_paddle.goto(-350, 0)
    r_paddle.goto(350, 0)
    is_paused = False

# Controls
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(toggle_pause, "p")     # Pause
screen.onkey(restart_game, "r")     # Restart

# Main game loop
while game_is_on:
    time.sleep(ball.move_Speed)
    screen.update()

    if not is_paused:
        ball.move()

        # Wall collision
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # Paddle collision
        if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
            ball.bounce_x()

        # Missed paddle
        if ball.xcor() > 380:
            ball.reset_ball()
            score.add_L_Score()

        if ball.xcor() < -380:
            ball.reset_ball()
            score.add_R_Score()

screen.exitonclick()
