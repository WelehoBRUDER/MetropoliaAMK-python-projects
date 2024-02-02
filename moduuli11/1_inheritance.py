class Julkaisu:
    def __init__(self, name):
        self.name: str = name


class Kirja(Julkaisu):
    def __init__(self, name, writer, pages):
        super().__init__(name)
        self.writer: str = writer
        self.pages: int = pages

    def print_info(self):
        print(f"Kirjan nimi: {self.name}")
        print(f"Kirjoittaja: {self.writer}")
        print(f"Sivujen määrä: {self.pages}")
        print("-" * 25)


class Lehti(Julkaisu):
    def __init__(self, name, head):
        super().__init__(name)
        self.head: str = head

    def print_info(self):
        print(f"Lehden nimi: {self.name}")
        print(f"Päätoimittaja: {self.head}")
        print("-" * 25)


def main():
    magazine = Lehti("Aku Ankka", "Aki Hyyppä")
    book = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

    magazine.print_info()
    book.print_info()


main()
