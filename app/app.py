from ast import Return
from flask import Flask, session, redirect, render_template, request
from flask_session import Session

app = Flask(__name__)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def  index():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def  login():
    if request.method ==  "POST":
        return redirect("citas")
    else:
        return render_template("login.html")

@app.route("/register")
def  register():
    return render_template("register.html")

@app.route("/citas")
def  citas():
    return render_template("citas.html")