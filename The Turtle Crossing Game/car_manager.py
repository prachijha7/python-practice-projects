from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_choice = random.randint(1,6)
        if random_choice == 1:
            new_car = Turtle(shape="square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            y_pos = random.randint(-250, 250)
            new_car.goto(300, y_pos)
            self.cars.append(new_car)

    def move_cars(self):
        for one_car in self.cars:
            x_pos = one_car.xcor() - self.car_speed
            one_car.setx(x_pos)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT

