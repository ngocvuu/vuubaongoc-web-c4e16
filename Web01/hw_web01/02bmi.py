from flask import Flask,render_template
app = Flask(__name__)

@app.route("/02bmi/<int:weight>/<int:height>")
def bmi(weight,height):
    h = height / 100
    BMI = weight / (h ** 2)
    return render_template("bmi.html",BMI=BMI)

if __name__== "__main__":
    app.run(debug=True)
