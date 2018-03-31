from flask import Flask
app = Flask(__name__)

@app.route("/bmi/<int:weight>/<int:height>")
def bmi(weight,height):
    h = height / 100
    BMI = weight / (h ** 2)
    if BMI < 16:
        return "Severely underweight"
    elif 18.5 <= BMI < 25:
        return "Normal"
    elif 25 <= BMI < 30:
        return "Overweight"
    else:
        return "Obese"


if __name__== "__main__":
    app.run(debug=True)
