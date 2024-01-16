import random

# Define the codes
three_numbers = ""
four_numbers = ""
# Loop x times to create a code
for i in range(3):
    three_numbers += str(random.randint(0, 9))
for i in range(4):
    four_numbers += str(random.randint(1, 6))
# Print result
print(f"Three number code: {three_numbers}")
print(f"Four number code: {four_numbers}")
