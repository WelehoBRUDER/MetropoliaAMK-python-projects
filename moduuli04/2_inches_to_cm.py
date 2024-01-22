def convert_inches_to_cm(inches):
    print(f"{inches} tuumaa on {inches * 2.54} cm")


user_input = 0
while user_input > -1:
    user_input = float(input("Anna tuumien määrä: "))
    if user_input > -1:
        convert_inches_to_cm(user_input)
