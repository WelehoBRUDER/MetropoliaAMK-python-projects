import random

class Elevator:
    def __init__(self, id, lowest_floor, highest_floor):
        self.id = id
        self.highest_floor = highest_floor
        self.lowest_floor = lowest_floor
        self.current_floor = lowest_floor

    def move_up(self):
        self.current_floor += 1
        if self.current_floor > self.highest_floor:
            self.current_floor = self.highest_floor
        print(f"Hissi {self.id} on kerroksessa {self.current_floor}.")

    def move_down(self):
        self.current_floor -= 1
        if self.current_floor < self.lowest_floor:
            self.current_floor = self.lowest_floor
        print(f"Hissi {self.id} on kerroksessa {self.current_floor}.")

    def move_to_floor(self, floor):
        if self.current_floor == floor:
          print(f"Hissi {self.id} on jo kerroksessa {floor}!")
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
    
    for i in range(0, elevators):
      self.elevators.append(Elevator(i + 1, self.lowest_floor, self.highest_floor))
      
    for elevator in self.elevators:
      print(f"Hissi {elevator.id}")
      
  def ride_elevator(self, num, floor):
    self.elevators[num - 1].move_to_floor(floor)
    
  def fire_alarm(self):
    print(f"{'#' * 25}\n{' ' * 7}PALOHÄLYTYS!\n{'#' * 25}")
    for i in range(0, len(self.elevators)):
      self.ride_elevator(i + 1, self.lowest_floor)
      print("-" * 25)

def main():
  lowest_floor = 1
  highest_floor = 20
  house = Talo(lowest_floor, highest_floor, 5)
  for i in range(0, len(house.elevators)):
    house.ride_elevator(i + 1, random.randint(lowest_floor, highest_floor))
    print("-" * 25)

  house.fire_alarm()

main()
