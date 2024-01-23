num = int(input("Anna kokonaisluku: "))
is_prime = True
# Check numbers between 2 and 10
for i in range(2, 10):
    # Exclude current number from the check, since it would pass
    if i != num:
        if num % i == 0:
            is_prime = False

print(f"Numero {num} {"on" if is_prime else "ei ole"} alkuluku")
