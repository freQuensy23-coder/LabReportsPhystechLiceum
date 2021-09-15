import turtle
from t10 import circle, n_angle

n = 6
R = 25
for i in range(n):
    turtle.left(180 - 360/n)
    turtle.forward(R)
    turtle.stamp()
    turtle.left(180)
    turtle.forward(R)


turtle.done()
