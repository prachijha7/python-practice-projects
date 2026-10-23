import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

tim.speed("fastest")
angle = 5
no_of_circles = int(360 / angle)
for circles in range(no_of_circles):
    tim.color(random_color())
    tim.circle(100)
    tim.left(angle)

my_screen = Screen()
my_screen.exitonclick()

