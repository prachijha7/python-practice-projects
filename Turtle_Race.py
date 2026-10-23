from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, - 40, -10, 20, 50, 80]
is_game_on = False
all_turtles = []

for t in range(0,6):   
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[t])
    new_turtle.penup()
    new_turtle.goto(x=-230, y = y_positions[t])
    all_turtles.append(new_turtle)

if user_bet:
    is_game_on = True

while is_game_on:

    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_game_on = False
            winner = turtle.pencolor()
            if user_bet == winner:
                print(f"You've won! The winner is {winner}!")
            else:
                print(f"You've lost! The winner is {winner}!")

        distance = random.randint(0, 10)
        turtle.forward(distance)
        
screen.exitonclick()