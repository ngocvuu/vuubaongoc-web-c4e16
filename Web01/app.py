from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    posts = [
        {
        "title" : "Thơ con ếch",
        "content": "con ếch là cậu ông trời",
        "author" : "ếch",
        "gender": 1
        },
        {
        "title": "Thơ trăng",
        "content" : "Hôm nay trăng cao quá, Anh muốn hôn em vào má",
        "author" : "Ta",
        "gender" : 1
        },
        {
        "title": "K biết làm thơ",
        "content" : "abc",
        "author" : "C. Hồng Anh",
        "gender" : 0
        }
    ]
    return render_template("index.html",
                            posts=posts)


@app.route("/hello")
def hello():
    return "Hello C4E16"

@app.route("/sayhi/<name>/<age>")
def sayhi(name, age):
    return "Hi " + name + ".You're " + age + " years old!"

@app.route("/sum/<int:x>/<int:y>")
def calc(x,y):
    return str(x + y)

if __name__ == '__main__':
  app.run(debug=True)
