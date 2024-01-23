def main():
    seasons = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi")
    month = int(input("Monesko kuukausi nyt on? (1-12): "))
    season = seasons[month - 1]
    print(f"Nyt on {season}")


main()
