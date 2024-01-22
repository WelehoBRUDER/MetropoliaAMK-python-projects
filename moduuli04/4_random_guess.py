import random

random_number = random.randint(1, 10)
user_guess = -1
while user_guess != random_number:
    user_guess = int(input("Arvaa numero 1-10 väliltä: "))
    if user_guess < random_number:
        print("Liian pieni arvaus")
    elif user_guess > random_number:
        print("Liian suuri arvaus")
    else:
        print("Oikein.")
