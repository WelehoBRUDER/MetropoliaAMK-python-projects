healthy_levels = {
    "N": (117, 175),
    "M": (134, 195)
}


def hemoglobin_check(sex, value):
    levels = healthy_levels[sex]
    level = "normaali"
    if value < levels[0]:
        level = "alhainen"
    elif value > levels[1]:
        level = "korkea"
    return print(f"Hemoglobiini arvosi on {level}")


user_sex_input = input("Mikä on biologinen sukupuolesi? (N tai M): ")
hemoglobin_level = int(input("Anna hemoglobiini arvosi (g/l): "))
hemoglobin_check(user_sex_input, hemoglobin_level)
