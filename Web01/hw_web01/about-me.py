import os
from flask import Flask,render_template,redirect
app = Flask(__name__)

@app.route("/about-me/")
def about():
    info = {
    "name" : "KLinh",
    "motto" : "Just keep swimming",
    "wish1": "học sinh cá biệt",
    "wish2": "against the world",
    "hobby": "sports"
    }
    return render_template("info.html", info=info)

@app.route("/school")
def school():
    return redirect("http://techkids.vn", code=302)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
