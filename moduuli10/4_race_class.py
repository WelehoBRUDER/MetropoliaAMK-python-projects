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
        
    def print_race_stats(self):
        print(f"Rekisteritunnus: {self.register}")
        print(f"Tämänhetkinen nopeus: {self.cur_speed} km/h")
        print(f"Kuljettu matka: {self.dist_traveled} km.")
        print("-" * 25)

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
        
class Kilpailu:
  def __init__(self, name, length, participants):
    self.name = name
    self.length = length
    self.participants = participants
    
  def pass_hour(self):
    for car in self.participants:
      car.accelerate(random.randint(-10, 15))
      car.drive(1)
      
  def print_status(self):
    for car in self.participants:
      car.print_race_stats()

  def is_race_over(self):
    over = False
    for car in self.participants:
      if car.dist_traveled > self.length:
        over = True
        break
    
    return over

def main():
    cars = []
    for i in range(10):
        car = Auto(f"ABC-{i}", random.randint(100, 200))
        cars.append(car)
        
    race = Kilpailu("Suuri romuralli", 8000, cars)
    time = 0
    race_ongoing = True
    while race_ongoing:
      race.pass_hour()
      time += 1
      race_ongoing = not race.is_race_over()
      if time % 10 == 0 or not race_ongoing:
        print(f"{'-' * 25}\n{' ' * 4}{time} tuntia kulunut!\n{'-' * 25}")
        race.print_status()


main()
