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
        stars = reviews.avarage("restaurant1")
        amount = reviews.amount("restaurant1")
        title = "Oljenkorsi"
        description = f"{ stars } stars from {amount} reviews."
        return render_template("restaurant.html", allreviews=allreviews, title=title, description=description)
    
    if request.method == "POST":
        username = session["username"]
        review = request.form["review"]
        stars = request.form["stars"]
        reviews.review("restaurant1", username, review, stars)
    return redirect("/restaurant1")

@app.route("/restaurant2", methods=["GET", "POST"])
def restaurant2():
    if request.method == "GET":
        allreviews = reviews.getreviews("restaurant2")
        stars = reviews.avarage("restaurant2")
        amount = reviews.amount("restaurant2")
        title = "Unicafe chemicum"
        description = f"{ stars } stars from {amount} reviews."
        return render_template("restaurant.html", allreviews=allreviews, title=title, description=description)
    
    if request.method == "POST":
        username = session["username"]
        review = request.form["review"]
        stars = request.form["stars"]
        reviews.review("restaurant2", username, review, stars)
    return redirect("/restaurant2")

@app.route("/restaurant3", methods=["GET", "POST"])
def restaurant3():
    if request.method == "GET":
        allreviews = reviews.getreviews("restaurant3")
        stars = reviews.avarage("restaurant3")
        amount = reviews.amount("restaurant3")
        title = "Unicafe physicum"
        description = f"{ stars } stars from {amount} reviews."
        return render_template("restaurant.html", allreviews=allreviews, title=title, description=description)
    
    if request.method == "POST":
        username = session["username"]
        review = request.form["review"]
        stars = request.form["stars"]
        reviews.review("restaurant3", username, review, stars)
    return redirect("/restaurant3")

@app.route("/restaurant4", methods=["GET", "POST"])
def restaurant4():
    if request.method == "GET":
        allreviews = reviews.getreviews("restaurant4")
        stars = reviews.avarage("restaurant4")
        amount = reviews.amount("restaurant4")
        title = "Unicafe exactum"
        description = f"{ stars } stars from {amount} reviews."
        return render_template("restaurant.html", allreviews=allreviews, title=title, description=description)
    
    if request.method == "POST":
        username = session["username"]
        review = request.form["review"]
        stars = request.form["stars"]
        reviews.review("restaurant4", username, review, stars)
    return redirect("/restaurant4")

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
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("register.html", message="Not the same password!")
        new = loginregister.registeruser(username, password1)
        if not new:
            return render_template("register.html", message = "Username taken!")
        else: 
            return redirect("/")
    
@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")



