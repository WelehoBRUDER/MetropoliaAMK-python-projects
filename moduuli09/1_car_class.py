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
        print(f"Kuljettu matka: {self.dist_traveled}")


def main():
    car = Auto("ABC-123", 142)
    car.print_stats()


main()
