num = int(input("Anna kokonaisluku: "))
is_prime = True
# Check numbers between 2 and n / 2
for i in range(2, int(num / 2) + 1):
    if num % i == 0:
        is_prime = False

print(f"Numero {num} {"on" if is_prime else "ei ole"} alkuluku")
