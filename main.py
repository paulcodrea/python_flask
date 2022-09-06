from flask import Flask, render_template
from stock_api import stock_api
import pandas as pd

app = Flask(__name__, template_folder='templates', static_folder='static')


# @app.route('/', methods=['GET'])
# def dropdown():
#     stocks = ['AAPL', 'TSLA', 'GOOGL', 'NMR']
#     return render_template('index.html', stocks=stocks)

@app.route("/")
def index():
  ticker = "NMR"
  with open("static/" + ticker + ".csv") as file:
    return render_template("stock.html", csv=file)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)
