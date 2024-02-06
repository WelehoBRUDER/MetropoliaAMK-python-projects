import mysql.connector
from flask import Flask

db = mysql.connector.connect(
    host="localhost"
    , user="root"
    , password="root"
    , database="flight_game"
)
operator = db.cursor(dictionary=True)

app = Flask(__name__)


def get_airport(code):
    operator.execute(
        f"SELECT ident as ICAO, name as Name, municipality as Municipality FROM airport WHERE ident = '{code}'")
    port_data = operator.fetchall()
    # It's not yet JSON, but can be converted from dict to JSON pretty easily.
    return port_data[0]


@app.route("/airport/<icao>", methods=["GET"])
def home(icao: str):
    airport = get_airport(icao)
    return f"<p>{airport}</p>"
