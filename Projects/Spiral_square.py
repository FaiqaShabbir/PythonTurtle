import turtle as tr

tr.pensize(2)
tr.speed(10)

length = 180

for j in range(90):

    # Making the turtle move forward by length (units)
    tr.fd(length)
    # As the exterior angle for a square is 90 degree,
    # thus using that to turn right
    tr.right(90)
    # Updating the new length as 2 units shorter
    # than the previous length
    length = length - 2
    tr.hideturtle()

tr.done()