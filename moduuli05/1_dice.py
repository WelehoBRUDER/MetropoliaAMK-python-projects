import random

total = 0
num_of_dice = int(input("Anna arpakuutioiden määrä: "))
for i in range(num_of_dice):
    dice = random.randint(1, 6)
    total += dice

print(f"Arpakuutioiden summa on {total}")
