import random


class Auto:
    def __init__(self, register, max_speed):
        self.register = register
        self.max_speed = max_speed
        self.cur_speed = 0
        self.dist_traveled = 0

    def print_stats(self):
        print(f"Rekisteritunnus: {self.register}")
        print(f"Huippunopeus: {self.max_speed} km/h")
        print(f"Tämänhetkinen nopeus: {self.cur_speed} km/h")
        print(f"Kuljettu matka: {self.dist_traveled} km.")

    def print_speed(self):
        print(f"Tämänhetkinen nopeus: {self.cur_speed} km/h")

    # Speed is in kilometers per hour
    def accelerate(self, speed):
        self.cur_speed += speed
        if self.cur_speed > self.max_speed:
            self.cur_speed = self.max_speed
        elif self.cur_speed < 0:
            self.cur_speed = 0

    # Time is given in hours
    def drive(self, time):
        self.dist_traveled += self.cur_speed * time


def main():
    cars = []
    goal = 10000
    highest_traveled = 0
    for i in range(10):
        car = Auto(f"ABC-{i}", random.randint(100, 200))
        cars.append(car)

    while highest_traveled < goal:
        for car in cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)
            if car.dist_traveled > highest_traveled:
                highest_traveled = car.dist_traveled

    for car in cars:
        car.print_stats()
        if car.dist_traveled >= goal:
            print("Kilpailun voittaja!")
        print("-" * 25)


main()
