from app import app
import reviews, loginregister, suggestions, followers
from flask import redirect, render_template, request, session, abort
import secrets

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        restaurants = reviews.getrestaurants()
        return render_template("index.html", restaurants=restaurants)

    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        finduser = request.form["username"]
        user = loginregister.checkuser(finduser)
        if user:
            return redirect("/profile/"+finduser)
        return render_template("index.html", message="User does not exist.")

@app.route("/profile/<string:username>", methods=["GET", "POST"])
def profile(username):
    user_id = loginregister.user_id(username)
    follower = followers.is_following(user_id)
    profilefollowers = followers.getfollowers(user_id)
    profilesuggestions = suggestions.getprofilesuggest(user_id)
    profilereviews = reviews.getprofilereviews(user_id)
    if request.method == "GET":
        return render_template("profile.html", username=username, profilesuggestions=profilesuggestions, profilereviews=profilereviews, profilefollowers=profilefollowers, follower=follower)
    
    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        request.form["followbtn"]
        if follower:
            followers.unfollow(user_id)
        else:
            result = followers.follow(user_id)
            if result:
                return redirect("/profile/"+username)
            return render_template("profile.html", message=result, username=username, profilesuggestions=profilesuggestions, profilereviews=profilereviews, profilefollowers=profilefollowers, follower=follower)
        return redirect("/profile/"+username)
        
@app.route("/restaurant/<int:id>", methods=["GET", "POST"])
def restaurant(id):
    if request.method == "GET":
        allreviews = reviews.getreviews(id)
        stars = reviews.avarage(id)
        amount = reviews.amount(id)
        title = "Oljenkorsi"
        description = f"{stars} stars from {amount} reviews."
        return render_template("restaurant.html", allreviews=allreviews, title=title, description=description, id=id)
    
    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        review = request.form["review"]
        stars = request.form["stars"]
        reviews.review(id, review, stars)
    return redirect("/restaurant/"+str(id))

@app.route("/suggestions", methods=["GET", "POST"])
def give_and_get_suggestions():
    if request.method == "GET":
        allsuggestions = suggestions.getsuggest()
        return render_template("suggestions.html", allsuggestions=allsuggestions)
    
    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        name = request.form["restaurant"]
        info = request.form["info"]
        suggestions.suggest(name, info)
    return redirect("/suggestions")

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
            session["user_id"] = loginregister.user_id(username)
            session["csrf_token"] = secrets.token_hex(16)
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



