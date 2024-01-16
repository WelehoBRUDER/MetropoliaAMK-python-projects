leiviskat = float(input("Leiviskien määrä: "))
naulat = float(input("Naulojen määrä: "))
luodit = float(input("Luotien määrä: "))
luoti_weight = 13.3

grams = leiviskat * 20 * 32 * luoti_weight
grams += naulat * 32 * luoti_weight
grams += luodit * luoti_weight

kilograms = int(grams / 1000)
grams = grams - (kilograms * 1000)
grams = '{0:.2f}'.format(grams)

print(f"Massa nykyisissä mitoissa: {kilograms}kg {grams} grammaa")
