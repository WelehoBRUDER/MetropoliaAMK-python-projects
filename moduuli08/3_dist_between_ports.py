import geopy.distance
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost"
    , user="root"
    , password="root"
    , database="flight_game"
)
operator = mydb.cursor()


def dist_between_airports(port_1, port_2):
    operator.execute(
        f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{port_1}' OR ident = '{port_2}'")
    airport_data = operator.fetchall()
    distance = geopy.distance.distance(airport_data[0], airport_data[1])
    return distance


def main():
    port1 = input("Anna ensimmäisen lentokentän ICAO-koodi: ")
    port2 = input("Anna toisen lentokentän ICAO-koodi: ")
    dist = dist_between_airports(port1, port2)
    print(f"Lentokenttien välinen matka on {dist}")


main()
