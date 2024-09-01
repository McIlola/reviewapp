from db import db
from sqlalchemy.sql import text
from flask import session

def follow(user_id):
    if user_id == session["user_id"]:
        return "You can't follow yourself"
    try:
        sql = text("INSERT INTO Followers (user_id, follow_id) VALUES (:user_id, :follow_id)")
        db.session.execute(sql, {"user_id":session["user_id"], "follow_id":user_id})
        db.session.commit()
    except:
        return "You are following that user"
    return True

def is_following(user_id):
    sql = text("SELECT * FROM Followers WHERE user_id=:user_id AND follow_id=:follow_id")
    result = db.session.execute(sql, {"user_id":session["user_id"], "follow_id":user_id}).fetchone()
    if result is None:
        return False
    else:
        return True
    
def getfollowers(user_id):
    sql = text("SELECT U.username FROM Followers F, Users U WHERE U.id=F.Follow_id AND F.user_id=:user_id")
    result = db.session.execute(sql, {"user_id":user_id}).fetchall()
    return result

def unfollow(user_id):
    sql = text("DELETE FROM Followers WHERE user_id=:user_id AND follow_id=:follow_id")
    db.session.execute(sql, {"user_id":session["user_id"], "follow_id":user_id})
    db.session.commit()