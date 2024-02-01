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
    car = Auto("ABC-123", 142)
    car.accelerate(30)
    car.accelerate(70)
    car.accelerate(50)
    car.drive(2)
    car.print_stats()
    car.drive(3.7)
    car.accelerate(-200)
    car.print_stats()


main()
