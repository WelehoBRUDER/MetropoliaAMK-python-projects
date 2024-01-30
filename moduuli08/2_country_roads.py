import mysql.connector

mydb = mysql.connector.connect(
    host="localhost"
    , user="root"
    , password="root"
    , database="flight_game"
)
operator = mydb.cursor()


def get_airport_count(iso):
    operator.execute(
        f"SELECT airport.type, COUNT(airport.type) FROM airport WHERE airport.iso_country = '{iso}' GROUP BY airport.type ORDER BY COUNT(airport.type) DESC")
    airport_data = operator.fetchall()
    return airport_data


def main():
    search = input("Anna halutun maan ISO-koodi: ")
    airport_data = get_airport_count(search)
    for airport in airport_data:
        name = airport[0]
        count = airport[1]
        print(f"Kokoa {name}: {count}")


main()
