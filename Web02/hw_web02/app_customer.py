from flask import Flask, render_template
from models.customers import Customers
import mlab

app = Flask(__name__)
mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/customer/<int:gender>")
def customer(gender):
    all_customers = Customers.objects[:10](contacted=False,gender=gender)
    return render_template("customer.html", all_customers=all_customers)

if __name__ == '__main__':
  app.run(debug=True)
