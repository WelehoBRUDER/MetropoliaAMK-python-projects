username = "python"
password = "rules"
username_input = ""
password_input = ""
attempts = 5
success = False
while (username_input != username or password_input != password) and attempts > 0:
    username_input = input("Käyttäjätunnus: ")
    password_input = input("Salasana: ")
    if username_input == username and password_input == password:
        success = True
        break
    attempts -= 1

if success:
    print("Tervetuloa")
else:
    print("Pääsy evätty")
