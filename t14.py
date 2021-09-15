from t10 import circle
import turtle
from math import sin, cos, pi

def calc_coord_n(n, l, CX, CY):
    """Расчитать координаты вершин правильного n-угольника. Cамый правый край правильного многоугольника вертикальный.
     n - количество ребер, l - длина стороны. Все вершины лежат на окружности с заданным центром (CX, CY). Работает как генератор
    :param n - количество вершин
    :param l - длинна стороны
    :param CX - х центра описаной окружности
    :param CY - y центра описаной окружности
    :returns (x, y) 
    """    
    R = l / (2 * sin(pi / n))
    for i in range(n):
        yield  CX + R * cos(pi/n * (1 + 2 * i)), CY + R * sin(pi/n * (1 + 2 * i))


L = 75

def linespace(start, n, step):
    for i in range(n+1):
        yield start + i * step

def star(n):
    """построить n-угольную звезду"""
    cords = list(calc_coord_n(n, L, 0,0))
    turtle.penup()
    turtle.goto(*cords[0])
    step = int(n/2)
    turtle.pendown()
    for i in linespace(0, n, step):
        turtle.goto(*cords[i % n])
        

if __name__ == "__main__":
    size = 5
    star(size)
    turtle.done()
