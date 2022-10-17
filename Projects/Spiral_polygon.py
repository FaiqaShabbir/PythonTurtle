import turtle as tr

tr.speed(150)
side = int(input("Enter total no of sides: "))
length = int(input("Enter total length of a side: "))
angle = 360/side

for j in range(55):

    # Making the turtle move forward by length (units)
    tr.forward(length)
    # Taking the exterior angle for a polygon as 360/sides
    # degrees
    tr.right(angle)
    # Updating the new length as 2 units shorter
    # than the previous length
    length = length - 2
    tr.hideturtle()


tr.done()
