import turtle as tr

tr.speed(150)
length = 4

for j in range(60):

    tr.fd(length)
    tr.right(120)
    length = length - 4
    print(length)
    tr.hideturtle()

tr.done()
