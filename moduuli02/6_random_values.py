import random

# This function generates a code with a set length
# It also accepts the set values as a tuple
def generateCode(length, vals):
    code = ""
    for i in range(length):
        code += str(random.randint(vals[0], vals[1]))
    return code


# Print result
print(f"Three number code: {generateCode(3, (0, 9))}")
print(f"Four number code: {generateCode(4, (1, 6))}")
