import random

radius = 1
number_of_points = int(input("Anna arvottavien pisteiden määrä: "))
points_in_circle = 0

for i in range(1, number_of_points):
    cords = {"x": random.uniform(-radius, radius), "y": random.uniform(-radius, radius)}
    if cords["x"] ** 2 + cords["y"] ** 2 < radius:
        points_in_circle += 1

pi_approximate = 4 * points_in_circle / number_of_points

print(f"Piin likiarvo on {pi_approximate}")
