# importing libraries
import turtle
import random
import time

"""
title() will set the desired title of the screen
setup() used to set the height and width of the screen
tracer(0) will turn off the screen update
bgcolor() will set the background color
forward() will use to move the turtle in a forwarding direction for a specified amount
right() used to turn the turtle clockwise and left() used to turn the turtle anticlockwise
penup() will not draw while its move
"""

# creating turtle screen
screen = turtle.Screen()
screen.title('DATAFLAIR-SNAKE GAME')
screen.setup(width=700, height=700)
screen.tracer(0)
turtle.bgcolor('turquoise')

# creating a border for our game

turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310, 250)
turtle.pendown()
turtle.color('black')
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()

"""
Turtle() will be used to create a new turtle object
hideturtle() will use to hide the turtle
goto() used to move the turtle at x and y coordinates
"""
# score
score = 0
delay = 0.1

# snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape('square')
snake.color("black")
snake.penup()
snake.goto(0, 0)
snake.direction = 'stop'

# food
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape('circle')
fruit.color('red')
fruit.penup()
fruit.goto(30, 30)

old_fruit = []

# scoring
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("black")
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 300)
scoring.write("Score :", align="center", font=("Courier", 24, "bold"))

"""
screen.listen() function listen when key will press.

If the Up key will press then the snake will move in up direction.

If the Down key is pressed then the snake will move in the down direction.

If Left key will press then the snake will move in left direction.
"""


# define how to move
def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"


def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"


def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"


def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"


def snake_move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)


# Keyboard bindings
screen.listen()
screen.onkeypress(snake_go_up, "Up")
screen.onkeypress(snake_go_down, "Down")
screen.onkeypress(snake_go_left, "Left")
screen.onkeypress(snake_go_right, "Right")

# main loop

while True:
    """
    If the snake touches the fruit then the fruit will go at any random position and score will increase and the size of the snake will also increase
    """

    screen.update()
    # snake and fruit collisions
    if snake.distance(fruit) < 20:
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)
        fruit.goto(x, y)
        scoring.clear()
        score += 1
        scoring.write("Score:{}".format(score), align="center", font=("Courier", 24, "bold"))
        delay -= 0.001

        # creating new_ball
        new_fruit = turtle.Turtle()
        new_fruit.speed(0)
        new_fruit.shape('square')
        new_fruit.color('red')
        new_fruit.penup()
        old_fruit.append(new_fruit)

    # adding ball to snake

    for index in range(len(old_fruit) - 1, 0, -1):
        a = old_fruit[index - 1].xcor()
        b = old_fruit[index - 1].ycor()

        old_fruit[index].goto(a, b)

    if len(old_fruit) > 0:
        a = snake.xcor()
        b = snake.ycor()
        old_fruit[0].goto(a, b)
    snake_move()

    """
    If the snake touches the border of the game then the game will over.

    screen.clear() will delete all the drawing of the turtle on the screen
    """
    # snake and border collision
    if snake.xcor() > 280 or snake.xcor() < -300 or snake.ycor() > 240 or snake.ycor() < -240:
        time.sleep(1)
        screen.clear()
        screen.bgcolor('turquoise')
        scoring.goto(0, 0)
        scoring.write("   GAME OVER \n Your Score is {}".format(score), align="center", font=("Courier", 30, "bold"))

    # snake collision
    for food in old_fruit:
        if food.distance(snake) < 20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor('turquoise')
            scoring.goto(0, 0)
            scoring.write("    GAME OVER \n Your Score is {}".format(score), align="center",
                          font=("Courier", 30, "bold"))

    time.sleep(delay)

turtle.Terminator()
