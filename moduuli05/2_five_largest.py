numbers = []

# Initialize answer to prevent loop from breaking instantly
answer = "-1"
while answer != "":
    answer = input("Anna luku: ")
    # Prevent crash from converting string
    try:
        numbers.append(int(answer))
    except ValueError:
        # This doesn't actually change anything
        # since the loop would break anyway
        break

numbers.sort(reverse=True)

for i in range(0, len(numbers)):
    # Break loop once we have shown 5 numbers
    if i >= 5:
        break
    print(numbers[i])
