import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
t.colormode(255)
colors = [ (202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20)]

def draw(x,y):
    tim.hideturtle()
    tim.penup()
    tim.goto(x,y)
    for _ in range(10):
        color = random.choice(colors)
        tim.dot(20, color)
        tim.forward(50)

start_x = -250
start_y = -250

for rows in range(10):
    draw(start_x,start_y + rows * 50)

my_screen = Screen()
my_screen.exitonclick()

