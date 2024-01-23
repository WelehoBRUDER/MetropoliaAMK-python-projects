def main():
    airports = {"EFHK": "Helsinki-Vantaa", "EFET": "Enontekiön lentoasema", "EFIV": "Ivalon lentoasema",
                "EFJO": "Joensuun lentoasema"}
    user_input = 0
    print("Valitse komento (1-3):")
    print("1 Lisää uusi lentoasema")
    print("2 Hae lentoasemaa")
    print("3 Lopeta")
    while user_input != 3:
        user_input = int(input("Komento: "))

        if user_input == 1:
            add_airports(airports)
        elif user_input == 2:
            find_airport(airports)


def add_airports(airports):
    icao_code = input("Anna lisättävän lentoaseman ICAO-koodi: ")
    name = input("Anna lisättävän lentoaseman nimi: ")
    airports[icao_code] = name
    print(f"Lentoasema {icao_code} lisätty")


def find_airport(airports):
    icao_code = input("Anna haettavan lentoaseman ICAO-koodi: ")
    if airports[icao_code]:
        print(f"Lentoaseman {icao_code} nimi on {airports[icao_code]}")
    else:
        print("Kyseistä lentoasemaa ei löytynyt")


main()
