import turtle as tr

tac = tr.Turtle()

tac.color("violet")
tac.width("7")
tac.speed(4)

# Initialising a for Loop for making the main
# outline square of length 150
for j in range(4):
    tac.fd(150)
    tac.lt(90)

# making lines inside the outline square
tac.penup()
tac.goto(0, 50)
tac.pendown()

tac.forward(150)

tac.penup()
tac.goto(0, 100)
tac.pendown()

tac.forward(150)

tac.penup()
tac.goto(50, 0)
tac.pendown()

tac.left(90)
tac.forward(150)

tac.penup()
tac.goto(100, 0)
tac.pendown()

tac.forward(150)

tac.hideturtle()
tr.done()
