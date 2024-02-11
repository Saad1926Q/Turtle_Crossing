import turtle,random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.cars=[]
        self.move_dist=STARTING_MOVE_DISTANCE

    def generate_car(self):
        random_chance=random.randint(1,3)
        if random_chance==3:
            new_car=turtle.Turtle(shape="square")
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300,random.randint(-240,260))
            new_car.setheading(180)
            self.cars.append(new_car)

    def move_car(self):
        for car in self.cars:
            car.forward(self.move_dist)

    def cars_reset(self):
        for car in self.cars:
            car.goto(1000,1000)
        self.cars.clear()
        self.move_dist=STARTING_MOVE_DISTANCE