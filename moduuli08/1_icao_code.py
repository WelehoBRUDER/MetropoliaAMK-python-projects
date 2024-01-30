import mysql.connector

mydb = mysql.connector.connect(
    host="localhost"
    , user="root"
    , password="root"
    , database="flight_game"
)
operator = mydb.cursor()


def get_airport_data(icao):
    operator.execute(f"SELECT name, municipality FROM airport WHERE ident = '{icao}'")
    airport_data = operator.fetchall()
    return airport_data[0]


def main():
    search = input("Anna lentokentän ICAO-koodi: ")
    airport_data = get_airport_data(search)
    name = airport_data[0]
    municipality = airport_data[1]
    print(f"{name} paikkakunnalla {municipality}")


main()
