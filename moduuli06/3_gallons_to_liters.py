def gallons_to_liters(gallons):
    return gallons * 3.785


def main():
    gallons_amount = 0
    while gallons_amount >= 0:
        gallons_amount = int(input("Montako galloonaa bensaa haluat muuntaa?: "))
        if gallons_amount >= 0:
            print(f"{gallons_amount} galloonaa on {'{:.3f}'.format(gallons_to_liters(gallons_amount))} litraa.")


main()
