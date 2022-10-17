import turtle as tr

star = tr.Turtle()
num_of_sides = 5
len_of_sides = 50
each_side_angle = 720.0/num_of_sides
star.color('red', 'green')
star.pensize(30)

for i in range(num_of_sides):
    star.forward(len_of_sides)
    star.rt(each_side_angle)

tr.done()
