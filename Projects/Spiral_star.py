import turtle as tr

tr.speed(1)

length = 4

for j in range(60):

    # Making the turtle move forward by length (units)
    tr.fd(length)
    # Taking the exterior angle for a star shape as -144 degree,
    # where -ve sign is used to draw the star upside down
    tr.rt(-144)
    # Updating the new length as 4 units shorter
    # than the previous length
    length = length - 4
    tr.hideturtle()

tr.done()
