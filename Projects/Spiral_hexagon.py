# Python program for drawing a Spiraling Polygon in Turtle
# Importing the turtle Python library
import turtle

trtl = turtle.Turtle()

# Taking the speed of turtle as 150
trtl.speed(150)

# Taking the length of the side as 2 initially
length = 2

# Iterating the drawing 48 times overall
for j in range(48):
    # Making the turtle move forward by length (units)
    trtl.forward(length)
    # Taking the exterior angle for a hexagon shape as 60 degrees
    trtl.right(60)
    # Updating the new length as 4 units shorter
    # than the previous length
    length = length - 4

# Hiding the turtle after the completion of our drawing
trtl.hideturtle()