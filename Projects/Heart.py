import turtle

turtle.bgcolor("black")
t = turtle.Turtle()
turtle.speed(-5)
t.color("red")
t.begin_fill()
t.fillcolor("purple")
t.left(140)
t.forward(180)
t.circle(-90, 200)
t.setheading(60)
t.circle(-90, 200)
t.forward(180)
t.end_fill()
t.write("@reempython", 'false', 'center', font=('Showcard gothic', 20))

turtle.done()
