from t10 import circle
import turtle

# turtle.left(90)
turtle.color('black', 'yellow')

def draw_face():
    turtle.begin_fill()
    circle(50)
    turtle.end_fill()

def draw_eyes():
    turtle.penup()
    turtle.goto(10,70)
    circle(10, fill_color="blue")
    turtle.penup()
    turtle.goto(-10, 70)
    circle(10, fill_color="blue", action=turtle.right)

def draw_month():
    turtle.width(3)
    turtle.penup()
    turtle.goto(30, 40)
    turtle.color("red")
    circle(30, action=turtle.right, number=50)

if __name__ == "__main__":
    draw_face()
    turtle.right(90)
    draw_eyes()
    draw_month()
