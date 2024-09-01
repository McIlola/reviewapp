from db import db
from sqlalchemy.sql import text
from flask import session

def getsuggest():
    sql = text("SELECT U.username, S.suggestion, S.info FROM Suggestions S, Users U WHERE S.user_id=U.id ORDER BY S.id DESC")
    suggestions = db.session.execute(sql).fetchall()
    return suggestions

def getprofilesuggest(user_id):
    sql = text("SELECT S.suggestion, S.info FROM Suggestions S WHERE S.user_id=:user_id")
    profilesuggestions = db.session.execute(sql, {"user_id": user_id}).fetchall()
    return profilesuggestions

def suggest(name, info):
    user_id = session["user_id"]
    sql = text("INSERT INTO Suggestions (suggestion, info, user_id) VALUES (:suggestion, :info, :user_id)")
    db.session.execute(sql, {"suggestion":name, "info":info, "user_id":user_id})
    db.session.commit()
