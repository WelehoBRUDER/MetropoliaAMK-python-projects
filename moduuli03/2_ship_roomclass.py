room_classes = {
    "LUX": "LUX on parvekkeellinen hytti yläkannella.",
    "A": "A on ikkunallinen hytti autokannen yläpuolella.",
    "B": "B on ikkunaton hytti autokannen yläpuolella.",
    "C": "C on ikkunaton hytti autokannen alapuolella."
}

selected_room = input("Valitse hyttiluokka (LUX, A, B, C): ")
# Make sure user input is in caps
selected_room = selected_room.upper()
if selected_room in room_classes:
    print(room_classes[selected_room])
else:
    print("Virheellinen hyttiluokka")
