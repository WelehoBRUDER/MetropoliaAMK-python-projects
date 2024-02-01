class Elevator:
    def __init__(self, highest_floor, lowest_floor):
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
            for i in range(floor, self.current_floor):
                self.move_down()

        else:
            for i in range(self.current_floor, floor):
                self.move_up()


def main():
    elevator = Elevator(25, 5)
    elevator.move_to_floor(17)
    elevator.move_to_floor(elevator.lowest_floor)


main()
