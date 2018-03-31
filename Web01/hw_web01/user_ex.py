from flask import Flask,render_template
app = Flask(__name__)

@app.route("/user/<username>")
def user(username):
    users = {
        "quy" :{
        "name" : "Dinh Cong Quy",
        "age" : 20
    },
        "tuananh" :{
        "name" : "Huynh Tuan Anh",
        "age" : 22
    }
    }

    if username in users:
        us = users[username]
        return render_template("user_ex.html",us=us)
    else:
        return "User not found"

if __name__== "__main__":
    app.run(debug=True)
