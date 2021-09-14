from t10 import circle
import turtle

if __name__=="__main__":
    turtle.left(90)
    for r in range(20, 100, 5):
        circle(r)
        circle(r, action=turtle.right)
    
