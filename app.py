from flask import Flask, request, render_template, redirect, session, flash, url_for
from forex_python.converter import CurrencyRates, CurrencyCodes, RatesNotAvailableError
from werkzeug.wrappers import Request, Response

app = Flask(__name__)

# Flask session cookies 
app.config['SECRET_KEY'] = "oh-so-secret"

rates = CurrencyRates()
codes = CurrencyCodes()

@app.route("/")
def get_homepage():
    """Return to homepage"""

    return render_template("index.html")

@app.route("/error")
def get_error():
    """Displays an error message if something goes wrong or codes and numbers are invalid"""

    msg = session["msg"]
    return render_template("error.html", msg=msg)

@app.route("/convert", methods=["POST"])
def convert_currency():
    """Route to form for conversion submissions"""

    from_curr = request.form.get("from-curr").upper()
    to_curr = request.form.get("to-curr").upper()
    # amount = request.form.get("amount").upper()

    # For error handling:

    try:
        amount = float(request.form["amount"])

    except ValueError:
        session["msg"] = "NOT A VALID AMOUNT!"
        return redirect("/error")

    try: 
        result = rates.convert(from_curr, to_curr, amount)

    except RatesNotAvailableError:
        if codes.get_symbol(from_curr) is None:
            session["msg"] = f"NOT A VALID CODE {from_curr}"
        else:
            session["msg"] = f"NOT A VALID CODE {to_curr}"
        return redirect("/error")

    symbol = codes.get_symbol(to_curr)
    session["result"] = result
    session["symbol"] = symbol
    return redirect("/result")

@app.route("/result")
def get_result():
    """Shows the result of the conversion"""

    result = session["result"]
    formatted_float = "{:.2f}".format(result)
    symbol = session["symbol"]

    return render_template("result.html", result=formatted_float, symbol=symbol)

# Flask Server code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
