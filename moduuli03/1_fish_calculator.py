def fish_checker():
    length_of_fish = int(input("Kuinka pitkä kuhasi on?: "))
    if (length_of_fish < 37):
        print(f"Laske kuha takaisin järveen. Pyydystämäsi kala on {37 - length_of_fish}cm liian lyhyt.")
    else:
        print("Kuhasi on tarpeeksi pitkä!")


fish_checker()
