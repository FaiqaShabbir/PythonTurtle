import turtle as tr

tr.bgcolor('black')
tr.pensize(2.5)
tr.speed(20)

for j in range(6):
    for color in ('violet', 'white', 'blue', 'green', 'yellow', 'orange', 'red'):
        tr.color(color)

        # Drawing a circle
        tr.circle(80)
        # Moving 10 pixels to the left every time
        # a circle is drawn for drawing the next one
        tr.left(10)
        # after done the wrk hide the turtle
        tr.hideturtle()


tr.done()
