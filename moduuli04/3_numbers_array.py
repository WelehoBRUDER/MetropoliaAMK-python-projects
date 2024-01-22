numbers = []
user_input = "1"

while user_input != "":
    user_input = input("Anna luku (tyhjä lopettaa ohjelman): ")
    if user_input != "":
        user_input = float(user_input)
        numbers.append(user_input)

smallest_number = min(numbers)
largest_number = max(numbers)
print(f"Pienin numero on {smallest_number} ja suurin numero on {largest_number}")
