from math import sqrt

from flask import Flask

app = Flask(__name__)


@app.route("/primenumber/<number>", methods=["GET"])
def prime_number_check(number=None):
    is_prime = True
    number = int(number)
    # Check numbers between 2 and n / 2
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            is_prime = False

    return f"<p>Number {number} is {"not" if not is_prime else ""} a prime number.</p>"
