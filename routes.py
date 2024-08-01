from app import app
import reviews, loginregister
from flask import redirect, render_template, request, session
from werkzeug.security import check_password_hash, generate_password_hash

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/restaurant1", methods=["GET", "POST"])
def restaurant1():
    if request.method == "GET":
        allreviews = reviews.getreviews("restaurant1")
        return render_template("restaurant1.html", allreviews=allreviews)
    
    if request.method == "POST":
        username = "stilltesting"
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
            return render_template("nouser.html")
        else:
            hash_value = user.password
            if check_password_hash(hash_value, password):
                session["username"] = username
                return redirect("/")
            else:
                return render_template("wrongpassword.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        hash_value = generate_password_hash(password)
        loginregister.registeruser(username, hash_value)
        return redirect("/")
    
@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")



