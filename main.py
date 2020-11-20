from flask import Flask, render_template, url_for, redirect, request, session, flash
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy

app = Flask(__name__)




@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:          
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"
    
@app . route ("/static-example/img")
def static_example_img () :
    start = "<img src" 
    url = url_for ('static', filename ='background.jpg')
    end = '" >'
    return start + url + end , 200

@app.route("/Home")
def home():
    return render_template("home.html")
    

@app.route("/Math")
def math():
    return render_template("math.html")

@app.route("/English")
def english():
    return render_template("english.html")

@app.route("/Science")
def science():
    return render_template("science.html")

@app.route("/History")
def history():
    return render_template("history.html")

@app.route("/Art")
def art():
    return render_template("art.html")

if __name__ == "__main__":
    app.run(debug=True)