from functools import partial
from math import sin
import turtle


def n_angle(R, n, action = turtle.left, number = None, fill_color=None):
    number = number or n # Какое количество сторон рисовать. По умолчанию - все
    a = 2 * R * sin(180/57.2958/n) # Сторона нугольника
    fi = 360/n # Угол поворота
    turtle.pendown()
    if fill_color:
        turtle.color("black", fill_color)
        turtle.begin_fill()
    for i in range(number):
        turtle.forward(a)
        action(fi)
    turtle.end_fill()
    
circle = partial(n_angle, n=100)

if __name__ == "__main__":
    n = 3
    R = 140
    de_fi = 360/n

    for i in range(3):
        circle(R)
        circle(R, action=turtle.right)
        turtle.left(60)
