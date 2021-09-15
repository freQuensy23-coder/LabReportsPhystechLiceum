import turtle
from t10 import n_angle

dr = 15
n = 10
start = 25
for r in range(start, n*dr + start, dr):
    n_angle(r, 4)
    turtle.penup()
    turtle.right(135)    
    turtle.forward(dr)
    turtle.left(135)
    turtle.pendown()
