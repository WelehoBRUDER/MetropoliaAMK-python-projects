def is_leap_year(year):
    if year % 100 == 0 and year % 400 == 0:
        return True
    elif year % 100 == 0 and year % 400 != 0:
        return False
    return year % 4 == 0


user_year = int(input("Anna vuosiluku: "))
print(f"Vuosi {user_year} {"on" if is_leap_year(user_year) else "ei ole"} karkausvuosi")
