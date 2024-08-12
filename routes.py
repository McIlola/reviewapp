from app import app
import reviews, loginregister
from flask import redirect, render_template, request, session

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/restaurant1", methods=["GET", "POST"])
def restaurant1():
    if request.method == "GET":
        allreviews = reviews.getreviews("restaurant1")
        return render_template("restaurant1.html", allreviews=allreviews)
    
    if request.method == "POST":
        username = session["username"]
        review = request.form["review"]
        stars = request.form["stars"]
        reviews.review1(username, review, stars)
    return redirect("/restaurant1")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = loginregister.getuser(username, password)    
        if not user:
            return render_template("login.html", message = "Wrong username or password!")
        else:
            session["username"] = username
            return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        loginregister.registeruser(username, password)
        return redirect("/")
    
@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")



