# Create a Python class representing a car with methods for accelerating and braking
class Car:
    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.current_speed = 0

    def accelerate(self, speed_increase):
        self.current_speed += speed_increase
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        print(f"The car accelerates to {self.current_speed} km/h.")

    def brake(self, speed_decrease):
        self.current_speed -= speed_decrease
        if self.current_speed < 0:
            self.current_speed = 0
        print(f"The car slows down to {self.current_speed} km/h.")

    def __str__(self):
        return f"{self.year} {self.model}, Current Speed: {self.current_speed} km/h"


my_car = Car("Tesla", 2022, 250)

print(my_car)
my_car.accelerate(50)
my_car.accelerate(220)
my_car.brake(100)
my_car.brake(200)

