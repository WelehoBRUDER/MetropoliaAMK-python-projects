import random


def roll_dice(sides):
    return random.randint(1, sides)


def main():
    dice_sides = int(input("Montako tahkoa nopassa on?: "))

    times_rolled = 0
    roll = 0
    while roll != dice_sides:
        times_rolled += 1
        roll = roll_dice(dice_sides)
        print(roll)
    print(f"The dice was rolled {times_rolled} times before hitting {dice_sides}!")


main()
