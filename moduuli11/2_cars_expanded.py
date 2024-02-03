class Car:
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
        

class ElectricCar(Car):
  def __init__(self, register, max_speed, battery: float):
            super().__init__(register, max_speed)
            # The battery's capacity is measured in kWh
            self.battery = battery
            
class CombustionCar(Car):
    def __init__(self, register, max_speed, tank: float):
            super().__init__(register, max_speed)
            # The tank's capacity is measured in litres
            self.tank = tank
            
         
def main():
  cars = [ElectricCar("ABC-15", 180, 52.5), CombustionCar("ACD-123", 165, 32.3)]
  for car in cars:
    car.accelerate(car.max_speed / 2)
  for _ in range(3):
    for car in cars:
      car.drive(1)
  for car in cars:
    car.print_race_stats()
    
    
main()