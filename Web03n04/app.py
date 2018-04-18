from flask import Flask, render_template, request, redirect, url_for, session
from models.service import Service, Customer, Order
import mlab
from datetime import *
from random import choice
app = Flask(__name__)
app.secret_key = "secret"
mlab.connect()



# create a document

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/admin")
def admin():
    services=Service.objects()
    return render_template("admin.html",services=services)

@app.route("/search/<int:gender>")
def search(gender):
    all_services = Service.objects(gender=gender)
    return render_template("search.html", all_services=all_services)

@app.route("/detail/<service_id>")
def detail(service_id):
    all_services = Service.objects.with_id(service_id)
    if "logged_in" in session:
        return render_template("detail.html",services=all_services)
    else:
        session["service_id"] = service_id
        return redirect(url_for("login"))
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        form = request.form
        username = form["username"]
        password = form["password"]
        user = Customer.objects(username=username,password=password).first()
        if user is not None:
            session["logged_in"] = str(user["id"])
            return redirect(url_for("admin"))
        else:
            return redirect(url_for("sign-in"))
@app.route("/new-service",methods=["GET","POST"])
def create():
    if request.method == "GET":
        return render_template("new_service.html")
    elif request.method == "POST":
        form = request.form
        name = form["name"]
        yob = form["yob"]
        phone = form["phone"]
        address = form["address"]
        status = form["status"]
        description = form["description"]
        measurements = form["measurements"]
        new_service = Service(name=name,
                                yob=yob,
                                phone=phone,
                                address=address,
                                status=status,
                                description=description,
                                measurements=measurements)

        new_service.save()
        return redirect(url_for("admin"))
@app.route("/update-service/<service_id>", methods=["GET","POST"])
def update(service_id):
    service_to_update = Service.objects.with_id(service_id)
    if request.method == "GET":
        return render_template("update_service.html", services= service_to_update)
    elif request.method == "POST":
        form = request.form
        name = form["name"]
        yob = form["yob"]
        phone = form["phone"]
        address = form["address"]
        status = form["status"]
        description = form["description"]
        measurements = form["measurements"]
        update_service = Service(name=name,
                                yob=yob,
                                phone=phone,
                                address=address,
                                status=status,
                                description=description,
                                measurements=measurements)

        update_service.save()
        return redirect(url_for("admin"))
@app.route("/sign-in", methods=["GET","POST"])
def signin():
    if request.method == "GET":
        return render_template("signin.html")
    elif request.method == "POST":
        form = request.form
        name = form["name"]
        email = form["email"]
        username = form["username"]
        password = form["password"]

        new_user = Customer(name=name,
                        email=email,
                        username=username,
                        password=password
        )
        new_user.save()
        return redirect(url_for("admin"))
@app.route("/order/<order_id>")
def order(order_id):
    serviceid = Service.objects.with_id(order_id)
    userid = Customer.objects.with_id(session["logged_in"])
    time = datetime.now()
    is_accepted = choice(["True","False"])

    new_order = Order(serviceid=serviceid,
                    userid=userid,
                    time=time,
                    is_accepted=is_accepted
    )
    new_order.save()
    return "Đã gửi yêu cầu"
if __name__ == '__main__':
  app.run(debug=True)
