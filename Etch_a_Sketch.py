import turtle as t
from turtle import Screen

tim = t.Turtle()
screen = Screen()
tim.speed("fastest")

def move_forward():
    tim.forward(10)

def move_backward():
    tim.back(10)

def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def rotate_clockwise():
    tim.right(10)

def rotate_counterclockwise():
    tim.left(10)
    
screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(clear_drawing, "c")
screen.onkey(rotate_clockwise, "d")
screen.onkey(rotate_counterclockwise, "a")

screen.exitonclick()