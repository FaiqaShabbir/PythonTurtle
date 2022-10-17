import turtle as tr

tr.speed(150)
length = 2

for j in range(50):

    tr.forward(length)
    tr.right(72)
    length = length - 4
    print(length)
    tr.hideturtle()

tr.done()
