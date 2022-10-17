import turtle as t

n=1
while n<=40:
    c = t.clone()
    t.color("magenta")
    c.color("red")
    t.circle(n+3)
    c.circle(n-1)
    n = n+1
