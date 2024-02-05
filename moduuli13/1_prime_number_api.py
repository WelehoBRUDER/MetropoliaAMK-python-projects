# Just testing for now
from flask import Flask

app = Flask(__name__)


@app.route("/primenumber/<number>", methods=["GET"])
def prime_number_check(number=None):
    # FIXME
    # This prime number checking code is incorrect and needs to be fixed!
    is_prime = True
    number = int(number)
    # Check numbers between 2 and 10
    for i in range(2, 10):
        # Exclude current number from the check, since it would pass
        if i != number:
            if number % i == 0:
                is_prime = False

    return f"<p>Number {number} is {"not" if not is_prime else ""} a prime number.</p>"
