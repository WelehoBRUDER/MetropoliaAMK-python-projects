import random


def roll_dice(sides):
    return random.randint(1, sides)


def main():
    dice_sides = int(input("Montako tahkoa nopassa on?: "))

    roll = 0
    while roll != dice_sides:
        roll = roll_dice(dice_sides)
        print(roll)


main()
