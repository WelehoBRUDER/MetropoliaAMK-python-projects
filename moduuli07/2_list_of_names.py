def main():
    names = set()
    name = " "
    while name != "":
        name = input("Syötä nimi: ")
        if name in names:
            print("Aiemmin syötetty nimi")
        else:
            print("Uusi nimi")
        names.add(name)

    for name in names:
        print(name)


main()
