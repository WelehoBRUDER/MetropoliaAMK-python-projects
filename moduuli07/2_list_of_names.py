def main():
    names = []
    name = " "
    while name != "":
        name = input("Syötä nimi: ")
        if name in names:
            print("Aiemmin syötetty nimi")
        else:
            print("Uusi nimi")
        names.append(name)

    names.sort()

    for name in names:
        print(name)


main()
