from math import sin, cos, pi
import turtle


def n_angle(x,u):
    g = 1
    while g < (x+1):
        turtle.left(360 / x)
        g = g + 1
        turtle.forward(u)
    turtle.right(90-(180/x))

dr=35
r_new = r = 33

for i in range(3, 13):
    turtle.penup()
    
    turtle.forward(dr)

    turtle.left(90 - (180 / i))
    turtle.pendown()

    n_angle(i,r)
    r = 2*(dr+(r / 2 / sin(pi / i))) * sin(pi / (1+i))
    
turtle.done()
