healthy_levels = {
    "female": (117, 175),
    "male": (134, 195)
}


def hemoglobin_check(sex, value):
    levels = healthy_levels[sex]
    level = "normaali"
    if value < levels[0]:
        level = "alhainen"
    elif value > levels[1]:
        level = "korkea"
    return print(f"Hemoglobiini arvosi on {level}")


sexes = ["female", "male"]
user_sex_input = int(input("Mikä on biologinen sukupuolesi? (0 nainen, 1 mies): "))
while user_sex_input < 0 or user_sex_input > 1:
    user_sex_input = int(input("Mikä on biologinen sukupuolesi? (0 nainen, 1 mies): "))
user_sex = sexes[user_sex_input]
hemoglobin_level = int(input("Anna hemoglobiini arvosi (g/l): "))
hemoglobin_check(user_sex, hemoglobin_level)
