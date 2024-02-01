import random

class Elevator:
    def __init__(self, lowest_floor, highest_floor):
        self.highest_floor = highest_floor
        self.lowest_floor = lowest_floor
        self.current_floor = lowest_floor

    def move_up(self):
        self.current_floor += 1
        if self.current_floor > self.highest_floor:
            self.current_floor = self.highest_floor
        print(f"Hissi on kerroksessa {self.current_floor}.")

    def move_down(self):
        self.current_floor -= 1
        if self.current_floor < self.lowest_floor:
            self.current_floor = self.lowest_floor
        print(f"Hissi on kerroksessa {self.current_floor}.")

    def move_to_floor(self, floor):
        if floor < self.current_floor:
            for _ in range(floor, self.current_floor):
                self.move_down()

        else:
            for _ in range(self.current_floor, floor):
                self.move_up()

class Talo:
  def __init__(self, lowest_floor, highest_floor, elevators):
    self.lowest_floor = lowest_floor
    self.highest_floor = highest_floor
    self.elevators = []
    
    for _ in range(0, elevators):
      self.elevators.append(Elevator(self.lowest_floor, self.highest_floor))
      
  def ride_elevator(self, num, floor):
    self.elevators[num - 1].move_to_floor(floor)

def main():
  lowest_floor = 1
  highest_floor = 20
  house = Talo(lowest_floor, highest_floor, 5)
  for i in range(0, len(house.elevators)):
    house.ride_elevator(i + 1, random.randint(lowest_floor, highest_floor))
    print("-" * 25)


main()
