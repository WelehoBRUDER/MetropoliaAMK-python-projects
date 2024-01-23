import math


# Diameter is assumed to be in centimeters
# and the price in euros
def calculate_pizza_price(diameter, price):
    # Calculate the radius of the pizza
    radius = (diameter / 2)
    # Calculate the area of the pizza in cm^2
    pizza_area = math.pi * radius ** 2
    # Calculate how many times the pizza fits in a m^2
    price_multiplier = 10 ** 4 / pizza_area
    # Returns the value of the pizza
    return price_multiplier * price


def main():
    pizza_1_diameter = float(input("Anna ensimmäisen pizzan halkaisija (cm): "))
    pizza_1_price = float(input("Anna ensimmäisen pizzan hinta (€): "))
    pizza_2_diameter = float(input("Anna toisen pizzan halkaisija (cm): "))
    pizza_2_price = float(input("Anna toisen pizzan hinta (€): "))

    # Get the values so we can compare them
    pizza_1_value = calculate_pizza_price(pizza_1_diameter, pizza_1_price)
    pizza_2_value = calculate_pizza_price(pizza_2_diameter, pizza_2_price)

    print(f"Pizza 1: {'{:.2f}'.format(pizza_1_value)}€/m^2")
    print(f"Pizza 2: {'{:.2f}'.format(pizza_2_value)}€/m^2")
    # The smaller number is better, because it means
    # that the price is cheaper when on an even size
    print(f"Pizza {"1" if pizza_1_value < pizza_2_value else "2"} antaa paremman vastineen rahallesi")


main()
